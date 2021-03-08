# -*- coding: utf-8 -*-
from unittest import mock

from click.testing import CliRunner

from saveme import cli


def test_cli_invalid_params():
    runner = CliRunner()
    result = runner.invoke(cli.run, ["--foo"])
    assert result.exit_code == 2
    assert result.output == 'Usage: run [OPTIONS]\nTry \'run --help\' for help.\n\nError: no such option: --foo\n' # noqa


@mock.patch('saveme.Saveme.run')
def test_cli(
    mock_saveme_app,
):
    runner = CliRunner()
    result = runner.invoke(cli.run, [])
    assert result.exit_code == 0
    mock_saveme_app.assert_called_once()
