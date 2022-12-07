"""Non-specific utility functions used by ``models`` and ``_manager``.

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

import typing


def setattrs(__obj: object, __names: typing.Iterable[str],
              __values: typing.Iterable[typing.Any], /) -> None:
    """Set ``__obj`` attribute given two iterables of corresponding names and
    values.
    
    """
    for k, v in zip(__names, __values):
        setattr(__obj, k, v)

def getnested(__target: dict, __keys: typing.Iterable, /) -> typing.Any:
    """Get a nested value of a target dictionary.
    
    """
    for k in __keys:
        try:
            __target = __target.get(k)
        except (KeyError, AttributeError):
            return
    return __target
