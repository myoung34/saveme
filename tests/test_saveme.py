# -*- coding: utf-8 -*-
""" main menubar object tests """

from unittest import mock

from rumps.rumps import Menu

import saveme


@mock.patch(
    'saveme.helpers.config.CONFIG.read',
    return_value=['/Users/foo/.aws/config']
)
@mock.patch(
    'saveme.helpers.config.CONFIG.sections',
    return_value=['sso_test']
)
def test_menu(
    mock_config_sections,
    mock_config_read,
):
    app = saveme.Saveme("saveme", icon='ns-icon.icns')
    assert app.menu == Menu()
    app.update_menu(mock.ANY)
    assert app.menu == {
        'Console Login': {
            'sso_test': {}
        },
        'Current profile None': {},
        'Quit': mock.ANY,
        'Start Metadata Server': {
            'sso_test': {}
        },
        'Stop Metadata Server': {}
     }
