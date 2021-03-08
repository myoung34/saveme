# -*- coding: utf-8 -*-
""" helper/config tests """

from unittest import mock

from rumps import MenuItem

from saveme.helpers import config


@mock.patch(
    'saveme.helpers.config.CONFIG.read',
    return_value=['/Users/foo/.aws/config']
)
@mock.patch(
    'saveme.helpers.config.CONFIG.sections',
    return_value=['sso_test']
)
def test_get_config(
    mock_config_sections,
    mock_config_read,
):
    config.get_profiles(mock.ANY)
    assert config.get_profiles(mock.ANY) == [
        MenuItem('sso_test', mock.ANY)
    ]
