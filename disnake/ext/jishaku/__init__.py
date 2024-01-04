# -*- coding: utf-8 -*-

"""
jishaku
~~~~~~~

A disnake.py extension including useful tools for bot development and debugging.

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

# pylint: disable=wildcard-import
from disnake.ext.jishaku.cog import *  # noqa: F401
from disnake.ext.jishaku.features.baseclass import Feature  # noqa: F401
from disnake.ext.jishaku.flags import Flags  # noqa: F401
from disnake.ext.jishaku.meta import *  # noqa: F401

__all__ = ("Jishaku", "Feature", "Flags", "setup")
