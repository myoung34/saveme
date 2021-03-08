# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# pylint: disable=global-statement
""" OSX Menu Bar for AWS-Vault Metadata Server (via launchctl) """

import logging
import os
import sys

from rumps import App, MenuItem, timer

from saveme.helpers.config import get_profiles
from saveme.helpers.vault import Vault

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

LOGGER = logging.getLogger()


class Saveme(App):
    """
    rumps OSX Menu app for aws-vault
    """
    def __init__(self, name: str, *args, **kwargs):
        """
        Initializer for rumps App
        @param name: Name of the Rumps Application
        @type name: str
        @param args: pass through args
        @type args: Tuple[Any, ...]
        @param kwargs: pass through kwargs
        @type kwargs: Dict[str, Any]
        """
        super().__init__(name, *args, **kwargs)
        self.vault = Vault()

    @timer(int(os.environ.get('UPDATE_FREQUENCY_SECONDS', 5)))
    def update_menu(self, _):
        """
        Function that runs on a timer to keep osx menu bar up to date
        @rtype: object
        """
        self.menu.clear()
        self.menu = [
            f'Current profile {self.vault.current_profile}',
            (
                'Console Login',
                get_profiles(self.vault.console_login)
            ),
            (
                'Start Metadata Server',
                get_profiles(self.vault.start_metadata_server)
            ),
            MenuItem(
                'Stop Metadata Server',
                callback=self.vault.stop_metadata_server
            ),
            APP.quit_button,
        ]


APP = Saveme("saveme", icon='ns-icon.icns')

if __name__ == "__main__":

    APP.run()  # pragma: no cover
