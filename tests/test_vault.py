# -*- coding: utf-8 -*-
""" helper/config tests """

from unittest import mock

from saveme.helpers import vault


class MockSender:
    @property
    def title(self):
        return 'wut'


def mocked_sender(*args, **kwargs):
    return MockSender()


class MockLoader:
    def __init__(self, profile='wut'):
        self.profile = profile


def mocked_loader(*args, **kwargs):
    return MockLoader()


@mock.patch(
    'rumps.rumps.MenuItem.title',
    side_effect=mocked_sender,
)
@mock.patch('os.system')
def test_console_login(
    mock_os_system,
    mock_menuitem_title,
):
    v = vault.Vault()
    v.console_login(mock_menuitem_title())
    mock_menuitem_title.assert_called_once()
    assert mock_os_system.mock_calls == [
        mock.call('aws-vault login wut')
    ]


def test_generate_launchagent(
):
    assert vault.generate_launchagent(profile_name='asdf') == '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n  <dict>\n    <key>Label</key>\n    <string>local.aws_vault_server</string>\n    <key>EnvironmentVariables</key>\n    <dict>\n      <key>AWS_VAULT_KEYCHAIN_NAME</key>\n      <string>aws-vault</string>\n    </dict>\n    <key>KeepAlive</key>\n    <true/>\n    <key>Program</key>\n    <string>/usr/local/bin/aws-vault</string>\n    <key>ProgramArguments</key>\n    <array>\n      <string>/usr/local/bin/aws-vault</string>\n      <string>exec</string>\n      <string>asdf</string>\n      <string>--no-daemonize</string>\n      <string>--server</string>\n      <string>--debug</string>\n    </array>\n    <key>RunAtLoad</key>\n    <false/>\n  </dict>\n</plist>\n'  # noqa


@mock.patch(
    'saveme.helpers.vault.generate_launchagent',
    return_value='<something/>',
)
@mock.patch(
    'saveme.helpers.vault.pathlib.PosixPath.expanduser',
    return_value='/Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist',
)
@mock.patch(
    'rumps.rumps.MenuItem.title',
    side_effect=mocked_sender,
)
@mock.patch(
    'os.path.exists',
    return_value=False,
)
@mock.patch('os.system')
def test_generate_launchagent_file_exists(
    mock_os_system,
    mock_path_exists,
    mock_menuitem_title,
    mock_expanduser,
    mock_generate_launchagent,
):
    with mock.patch("builtins.open", create=True):
        v = vault.Vault()
        v.start_metadata_server(mock_menuitem_title())
        assert mock_path_exists.mock_calls == [
            mock.call('/Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist')  # noqa
        ]
        mock_menuitem_title.assert_called_once()
        assert mock_generate_launchagent.mock_calls == [mock.call('wut')]
        assert mock_os_system.mock_calls == [
            mock.call('launchctl load -w /Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist')  # noqa
        ]


@mock.patch(
    'saveme.helpers.vault.generate_launchagent',
    return_value='<something/>',
)
@mock.patch(
    'saveme.helpers.vault.pathlib.PosixPath.expanduser',
    return_value='/Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist',
)
@mock.patch(
    'rumps.rumps.MenuItem.title',
    side_effect=mocked_sender,
)
@mock.patch(
    'os.path.exists',
    return_value=True,
)
@mock.patch('os.system')
def test_generate_launchagent_file_not_exists(
    mock_os_system,
    mock_path_exists,
    mock_menuitem_title,
    mock_expanduser,
    mock_generate_launchagent,
):
    with mock.patch("builtins.open", create=True):
        v = vault.Vault()
        v.start_metadata_server(mock_menuitem_title())
        assert mock_path_exists.mock_calls == [
            mock.call('/Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist')  # noqa
        ]
        mock_expanduser.assert_called_once()
        mock_menuitem_title.assert_called_once()
        assert mock_generate_launchagent.mock_calls == []
        assert mock_os_system.mock_calls == [
            mock.call('launchctl load -w /Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist')  # noqa
        ]


@mock.patch(
    'rumps.rumps.MenuItem.title',
    side_effect=mocked_sender,
)
@mock.patch(
    'saveme.helpers.vault.pathlib.PosixPath.expanduser',
    return_value='/Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist',
)
@mock.patch('os.system')
@mock.patch('os.remove')
def test_stop_metadata_server_file_exists(
    mock_os_remove,
    mock_os_system,
    mock_expanduser,
    mock_menuitem_title,
):
    v = vault.Vault()
    v.stop_metadata_server(mock_menuitem_title())
    mock_expanduser.assert_called_once()
    mock_menuitem_title.assert_called_once()
    assert mock_os_remove.mock_calls == [
        mock.call('/Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist')
    ]
    assert mock_os_system.mock_calls == [
        mock.call('launchctl unload /Users/foo/Library/LaunchAgents/local.aws_vault_wut.plist')  # noqa
    ]
