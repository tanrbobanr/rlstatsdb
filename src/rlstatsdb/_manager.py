"""The main systems used insert new entries into the database.

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

from . import constants
from . import models
from . import utils
import sqlite3
import datetime


def _getts(__datestr: str, /) -> int:
    """Get the timestamp of the given datestring (ISO).
    
    """
    return int(datetime.datetime.fromisoformat(__datestr).timestamp())


def _create_table(db_cur: sqlite3.Cursor, table: str, colnames: list[str],
                  coltypes: list[str]) -> None:
    """Create a table with the given name, column names, and column types.
    
    """
    col_statements = [f"{c} {t}" for c, t in zip(colnames, coltypes)]
    db_cur.execute(f"CREATE TABLE IF NOT EXISTS {table} "
                   f"({', '.join(col_statements)})")

  
def _ensure_tables_exist(db_conn: sqlite3.Connection) -> None:
    """Ensure all required tables (PLAYERS, TEAMS, MANIFEST) exist, else create.
    
    """
    db_cur = db_conn.cursor()
    _create_table(db_cur, "PLAYERS", constants.colnames_players,
                  constants.coltypes_players)
    _create_table(db_cur, "TEAMS", constants.colnames_teams,
                  constants.coltypes_teams)
    _create_table(db_cur, "MANIFEST", constants.colnames_manifest,
                  constants.coltypes_manifest)
    db_conn.commit()


def _make_series(data: dict, locs: list[tuple[str, ...]]) -> list:
    """Get a series of data from ``data`` given multiple locations of one or
    more strings (dict keys).
    
    """
    return [utils.getnested(data, keyset) for keyset in locs]


def _make_player_series(__pdata: dict, __manifest_id: int,
                        __team: str, /) -> list:
    """Serialize a player dictionary in preparation for database insertion.
    
    """
    return [__manifest_id, 0 if __team == "blue" else 1] + _make_series(__pdata,
                                                  constants.dictlocs_players)


def _add_player(__db_conn: sqlite3.Connection, __pdata: dict, __manifest_id: int,
                __team: str) -> None:
    """Serialize and insert a player dictionary into the database.
    
    """
    db_cur = __db_conn.cursor()
    colnames = constants.colnames_players[1:] # don't include auto incr id
    player_series = _make_player_series(__pdata, __manifest_id, __team)
    wildcards = ["?"] * len(player_series)
    db_cur.execute(f"INSERT INTO PLAYERS ({','.join(colnames)}) VALUES"
                   f" ({','.join(wildcards)})", tuple(player_series))


def _make_team_series(__tdata: dict, __manifest_id: int,
                      __team: str, /) -> list:
    """Serialize a team dictionary in preparation for database insertion.
    
    """
    return [__manifest_id, 0 if __team == "blue" else 1] + _make_series(__tdata,
                                                  constants.dictlocs_teams)


def _add_team(__db_conn: sqlite3.Connection, __tdata: dict, __manifest_id: int,
                __team: str) -> None:
    """Serialize and insert a team dictionary into the database.
    
    """
    db_cur = __db_conn.cursor()
    colnames = constants.colnames_teams[1:] # don't include auto incr id
    team_series = _make_team_series(__tdata, __manifest_id, __team)
    wildcards = ["?"] * len(team_series)
    db_cur.execute(f"INSERT INTO TEAMS ({','.join(colnames)}) VALUES"
                   f" ({','.join(wildcards)})", tuple(team_series))


def _make_manifest_series(__rdata: dict) -> list:
    """Serialize a replay dictionary in preparation for database insertion.
    
    """
    series = _make_series(__rdata, constants.dictlocs_manifest)
    series.insert(13, _getts(__rdata["created"]))
    series.insert(13, _getts(__rdata["date"]))
    return series


def _add_manifest(__db_conn: sqlite3.Connection, __rdata: dict) -> int:
    """Serialize and insert a replay dictionary into the database.
    
    """
    db_cur = __db_conn.cursor()
    colnames = constants.colnames_manifest[1:] # don't include auto incr id
    manifest_series = _make_manifest_series(__rdata)
    wildcards = ["?"] * len(manifest_series)
    db_cur.execute(f"INSERT INTO MANIFEST ({','.join(colnames)}) VALUES"
                   f" ({','.join(wildcards)})", tuple(manifest_series))
    return db_cur.lastrowid
    

class Manager:
    """The main class used to insert and get replay stats.
    
    """
    def __init__(self, db_path: str) -> None:
        """
        Arguments
        ---------
        db_path : str
            The path to the SQLite database (or empty file).
        
        """
        self.db_path = db_path
        _ensure_tables_exist(self._db_conn)
    
    @property
    def _db_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        return conn
    
    def add(self, replay_data: dict) -> int:
        """Add a replay dictionary to the database.

        Arguments
        ---------
        replay_data : dict
            Replay data as returned from ballchasing.com/api/replays/<id>
        
        Returns
        -------
        int
            The manifest ID
        
        """
        db_conn = self._db_conn
        uid = _add_manifest(db_conn, replay_data)
        for team in ("blue", "orange"):
            tdata = replay_data[team]
            _add_team(db_conn, tdata, uid, team)
            for pdata in tdata["players"]:
                _add_player(db_conn, pdata, uid, team)
        db_conn.commit()
        db_conn.close()
        return uid
    
    def get(self, manifest_id: int) -> models.Game:
        """Get a replay at the given manifest ID as a ``Game`` object.

        Arguments
        ---------
        manifest_id : int
            A valid manifest ID.
        
        """
        db_conn = self._db_conn
        db_cur = db_conn.cursor()
        mdata = db_cur.execute("SELECT * FROM MANIFEST WHERE id=?",
                               (manifest_id,)).fetchone()
        if not mdata:
            raise ValueError(f"entry with manifest ID of {manifest_id} does not exist")
        t0data, t1data = db_cur.execute("SELECT * FROM TEAMS WHERE "
                                        "manifest_id=? ORDER BY team ASC",
                                        (manifest_id,)).fetchall()
        p0data = db_cur.execute("SELECT * FROM PLAYERS WHERE manifest_id=? "
                                "AND team=?", (manifest_id, 0)).fetchall()
        p1data = db_cur.execute("SELECT * FROM PLAYERS WHERE manifest_id=? "
                                "AND team=?", (manifest_id, 1)).fetchall()
        db_conn.close()
        return models.Game(mdata, t0data, t1data, p0data, p1data)
    
    def remove(self, manifest_id: int) -> None:
        db_conn = self._db_conn
        db_cur = db_conn.cursor()
        db_cur.execute("DELETE FROM MANIFEST WHERE id=?", (manifest_id,))
        db_cur.execute("DELETE FROM TEAMS WHERE manifest_id=?", (manifest_id,))
        db_cur.execute("DELETE FROM PLAYERS WHERE manifest_id=?", (manifest_id,))
        db_conn.commit()
        db_conn.close()
