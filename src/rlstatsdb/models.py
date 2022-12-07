"""Models used to turn serialized data from the database into easy-to-navigate
classes representing the original replay format (as returned by
ballchasing.com's API).

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

import typing
from . import constants
from . import utils
from . import types


class Rank(types.Rank):
    __slots__ = constants.attrs_Rank
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_Rank, __data)

class Id(types.Id):
    __slots__ = constants.attrs_Id
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_Id, __data)

class Camera(types.Camera):
    __slots__ = constants.attrs_Camera
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_Camera, __data)

class PStats_core(types.PStats_core):
    __slots__ = constants.attrs_PStats_core
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_PStats_core, __data)

class PStats_boost(types.PStats_boost):
    __slots__ = constants.attrs_PStats_boost
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_PStats_boost, __data)

class PStats_movement(types.PStats_movement):
    __slots__ = constants.attrs_PStats_movement
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_PStats_movement, __data)

class PStats_positioning(types.PStats_positioning):
    __slots__ = constants.attrs_PStats_positioning
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_PStats_positioning, __data)

class PStats_demo(types.PStats_demo):
    __slots__ = constants.attrs_PStats_demo
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_PStats_demo, __data)

class TStats_ball(types.TStats_ball):
    __slots__ = constants.attrs_TStats_ball
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_TStats_ball, __data)

class TStats_core(types.TStats_core):
    __slots__ = constants.attrs_TStats_core
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_TStats_core, __data)

class TStats_boost(types.TStats_boost):
    __slots__ = constants.attrs_TStats_boost
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_TStats_boost, __data)

class TStats_movement(types.TStats_movement):
    __slots__ = constants.attrs_TStats_movement
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_TStats_movement, __data)

class TStats_positioning(types.TStats_positioning):
    __slots__ = constants.attrs_TStats_positioning
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_TStats_positioning, __data)

class TStats_demo(types.TStats_demo):
    __slots__ = constants.attrs_TStats_demo
    def __init__(self, __data: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_TStats_demo, __data)

class PStats(types.PStats):
    __slots__ = ("core", "boost", "movement", "positioning", "demo")
    def __init__(self, __data: typing.Iterable) -> None:
        self.core = PStats_core(__data[:9])
        self.boost = PStats_boost(__data[9:37])
        self.movement = PStats_movement(__data[37:55])
        self.positioning = PStats_positioning(__data[55:82])
        self.demo = PStats_demo(__data[82:])

class TStats(types.TStats):
    __slots__ = ("ball", "core", "boost", "movement", "positioning", "demo")
    def __init__(self, __data: typing.Iterable) -> None:
        self.ball = TStats_ball(__data[5:7])
        self.core = TStats_core(__data[7:15])
        self.boost = TStats_boost(__data[15:37])
        self.movement = TStats_movement(__data[37:46])
        self.positioning = TStats_positioning(__data[46:53])
        self.demo = TStats_demo(__data[53:])

class Player(types.Player):
    __slots__ = constants.attrs_Player + ["id", "rank", "camera", "stats"]
    def __init__(self, __pdata: typing.Iterable) -> None:
        utils.setattrs(self, constants.attrs_Player, __pdata[3:9])
        self.id = Id(__pdata[9:11])
        self.rank = Rank(__pdata[11:15])
        self.camera = Camera(__pdata[15:22])
        self.stats = PStats(__pdata[22:])

class Team(types.Team):
    __slots__ = constants.attrs_Team + ["players", "stats"]
    def __init__(self, __tdata: typing.Iterable,
                 __pdata: typing.Iterable[typing.Iterable]) -> None:
        utils.setattrs(self, constants.attrs_Team, __tdata[3:5])
        self.players = [Player(p) for p in __pdata]
        self.stats = TStats(__tdata)

class Game(types.Game):
    __slots__ = constants.attrs_Game + ["min_rank", "max_rank", "blue",
                                        "orange"]
    def __init__(self, __mdata: typing.Iterable, __t0data: typing.Iterable,
                 __t1data: typing.Iterable,
                 __p0data: typing.Iterable[typing.Iterable],
                 __p1data: typing.Iterable[typing.Iterable]) -> None:
        utils.setattrs(self, constants.attrs_Game, __mdata[0:16])
        self.min_rank = Rank(__mdata[16:20])
        self.max_rank = Rank(__mdata[20:])
        self.blue = Team(__t0data, __p0data)
        self.orange = Team(__t1data, __p1data)
