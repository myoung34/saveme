# -*- coding: utf-8 -*-
""" Generic configuration helpers """

import configparser
import pathlib
from typing import List

from rumps import MenuItem

CONFIG = configparser.RawConfigParser()


def get_profiles(callback: object) -> List[MenuItem]:
    """
    Parse AWS Config and generate rumps MenuItem list

    @type callback: object
    @rtype: MenuItem[]
    """
    path = pathlib.PosixPath('~/.aws/config')
    CONFIG.read(path.expanduser())
    profile_items = []
    for profile in CONFIG.sections():
        profile_items.append(MenuItem(
            profile.replace('profile ', ''),
            callback=callback
        ))
    return profile_items
