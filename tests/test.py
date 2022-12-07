import sys
sys.path.append(".")
from src import rlstatsdb
from src.rlstatsdb import constants
import json
import os




try:
    with open("tests/sdb", "a") as file:
        pass
    sdb = rlstatsdb.Manager("tests/sdb")
    with open("tests/test.json", "r") as infile:
        JSON = json.load(infile)
    sdb.add(JSON)
    GAME = sdb.get(1)
    
    # check minmax rank
    for K in constants.attrs_Rank:
        assert getattr(GAME.min_rank, K) == JSON["min_rank"][K], f"{GAME.min_rank.__qualname__}: {K}"
    for K in constants.attrs_Rank:
        assert getattr(GAME.max_rank, K) == JSON["max_rank"][K], f"{GAME.max_rank.__qualname__}: {K}"
    
    # check other GAME attrs
    assert GAME.replay_id == JSON["id"], "replay_id"
    assert GAME.uploader__steam_id == JSON["uploader"]["steam_id"], "uploader__steam_id"
    assert GAME.rocket_league_id == JSON["rocket_league_id"], "rocket_league_id"
    assert GAME.match_guid == JSON["match_guid"], "match_guid"
    assert GAME.title == JSON["title"], "title"
    assert GAME.map_code == JSON["map_code"], "map_code"
    assert GAME.match_type == JSON["match_type"], "match_type"
    assert GAME.team_size == JSON["team_size"], "team_size"
    assert GAME.playlist_id == JSON["playlist_id"], "playlist_id"
    assert GAME.duration == JSON["duration"], "duration"
    assert GAME.season == JSON["season"], "season"
    assert GAME.season_type == JSON["season_type"], "season_type"

    # iter teams
    for TEAMCOLOR in ("blue", "orange"):
        T: rlstatsdb.Team = getattr(GAME, TEAMCOLOR)
        JSONT = JSON[TEAMCOLOR]
        # check team
        assert getattr(T, "color") == JSONT["color"], f"{T.__qualname__}: color"
        for K in constants.attrs_TStats_ball:
            assert getattr(T.stats.ball, K) == JSONT["stats"]["ball"][K], f"{T.stats.ball.__qualname__}: {K}"
        for K in constants.attrs_TStats_core:
            assert getattr(T.stats.core, K) == JSONT["stats"]["core"][K], f"{T.stats.core.__qualname__}: {K}"
        for K in constants.attrs_TStats_boost:
            assert getattr(T.stats.boost, K) == JSONT["stats"]["boost"][K], f"{T.stats.boost.__qualname__}: {K}"
        for K in constants.attrs_TStats_movement:
            assert getattr(T.stats.movement, K) == JSONT["stats"]["movement"][K], f"{T.stats.movement.__qualname__}: {K}"
        for K in constants.attrs_TStats_positioning:
            assert getattr(T.stats.positioning, K) == JSONT["stats"]["positioning"][K], f"{T.stats.positioning.__qualname__}: {K}"
        for K in constants.attrs_TStats_demo:
            assert getattr(T.stats.demo, K) == JSONT["stats"]["demo"][K], f"{T.stats.demo.__qualname__}: {K}"

        # check players in team
        for i, P in enumerate(T.players):
            JSONP = JSONT["players"][i]
            for K in constants.attrs_Player:
                assert getattr(P, K) == JSONP[K], f"{P.__qualname__}: {K}"
            for K in constants.attrs_Id:
                assert getattr(P.id, K) == JSONP["id"][K], f"{P.id.__qualname__}: {K}"
            for K in constants.attrs_Rank:
                assert getattr(P.rank, K) == JSONP["rank"][K], f"{P.rank.__qualname__}: {K}"
            for K in constants.attrs_Camera:
                assert getattr(P.camera, K) == JSONP["camera"][K], f"{P.camera.__qualname__}: {K}"
            for K in constants.attrs_PStats_core:
                assert getattr(P.stats.core, K) == JSONP["stats"]["core"][K], f"{P.stats.core.__qualname__}: {K}"
            for K in constants.attrs_PStats_boost:
                assert getattr(P.stats.boost, K) == JSONP["stats"]["boost"][K], f"{P.stats.boost.__qualname__}: {K}"
            for K in constants.attrs_PStats_movement:
                assert getattr(P.stats.movement, K) == JSONP["stats"]["movement"][K], f"{P.stats.movement.__qualname__}: {K}"
            for K in constants.attrs_PStats_positioning:
                assert getattr(P.stats.positioning, K) == JSONP["stats"]["positioning"][K], f"{P.stats.positioning.__qualname__}: {K}"
            for K in constants.attrs_PStats_demo:
                assert getattr(P.stats.demo, K) == JSONP["stats"]["demo"][K], f"{P.stats.demo.__qualname__}: {K}"

    os.remove("tests/sdb")
except Exception as exc:
    os.remove("tests/sdb")
    raise exc
