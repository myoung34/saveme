# -*- coding: utf-8 -*-
""" Generic vault related helpers """

import os
import pathlib
from typing import Any

import chameleon
from rumps import MenuItem
from shellescape import quote


def generate_launchagent(profile_name: str) -> str:
    """
    Generate the launchctl launchagent xml
    """
    path = os.path.dirname(__file__)
    templates: chameleon.PageTemplateLoader = chameleon.PageTemplateLoader(
        os.path.join(path, "../templates")
    )
    template: Any = templates['launchagent.pt']
    launchagent_xml: str = template(profile=profile_name)
    return launchagent_xml


class Vault:
    """
    Vault class to handle aws-vault related actions
    """
    def __init__(self) -> None:
        """
        Initializer for Vault class
        """
        self.current_profile = 'None'

    def start_metadata_server(self, sender: MenuItem) -> None:
        """
        Start the launchctl aws-vault metadata server for the selected profile
        @param sender:
        @type sender:
        @return:
        @rtype:
        """
        self.current_profile = sender.title
        launchctl_path = pathlib.PosixPath(
            f'~/Library/LaunchAgents/local.aws_vault_{quote(sender.title)}.plist'  # noqa
        ).expanduser().__str__()
        if not os.path.exists(launchctl_path):
            with open(launchctl_path, "w") as launchctl_file:
                launchctl_file.write(
                    generate_launchagent(self.current_profile)
                )

        os.system(f'launchctl load -w {launchctl_path}')  # nosec

    def stop_metadata_server(self, sender: Any) -> None:  # pylint: disable=unused-argument  # noqa
        """
        Stop the launchctl aws-vault metadata server for
        the currently loaded profile

        @param sender: rumps sender
        @type sender: Any
        @return: None
        @rtype: None
        """
        launchctl_path = pathlib.PosixPath(
            f'~/Library/LaunchAgents/local.aws_vault_{quote(self.current_profile)}.plist'  # noqa
        ).expanduser()
        os.system(f'launchctl unload {launchctl_path}')  # nosec
        self.current_profile = 'None'
        os.remove(launchctl_path)

    def console_login(self, sender: Any) -> None:
        """
        Launch the aws-vault login command for the selected profile

        @param sender: rumps sender
        @type sender: Any
        @return: None
        @rtype: None
        """
        self.current_profile = sender.title
        os.system(f"aws-vault login {quote(sender.title)}")  # nosec
