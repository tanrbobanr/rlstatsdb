"""A simple and pythonic system to store, retrieve, and analyze Rocket League
replay stats as returned from ballchasing.com's API.

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

__title__ = "rlstatsdb"
__author__ = "Tanner B. Corcoran"
__email__ = "tannerbcorcoran@gmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022 Tanner B. Corcoran"
__version__ = "0.0.2"
__description__ = ("A simple and pythonic system to store, retrieve, and "
                   "analyze Rocket League replay stats as returned from "
                   "ballchasing.com's API.")
__url__ = "https://github.com/tanrbobanr/rlstatsdb"
__download_url__ = "https://pypi.org/project/rlstatsdb/"


from ._manager import Manager
from .models import Game
from .models import Player
from .models import Team
from .models import Rank
from .models import Id
from .models import Camera
from .models import PStats
from .models import TStats
