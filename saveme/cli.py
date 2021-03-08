# -*- coding: utf-8 -*-
""" Main Click methods """

import configparser
import logging
import sys

import click

from saveme import APP, LOGGER

CONFIG = configparser.ConfigParser()


@click.command()
@click.option(
    '--config-file',
    '-c',
    default='config.ini',
    help="configuration file path",
)
def run(
    config_file: str = 'config.ini',
) -> None:
    """
    Click entrypoint to launch menu app

    @param config_file: Config file location
    @type config_file: str
    @rtype: None
    """
    CONFIG.read(config_file)

    handler = logging.StreamHandler(sys.stdout)
    logging_level = 'INFO'
    try:
        logging_level = CONFIG['general'].get('logging_level', 'INFO')
    except KeyError:
        pass
    LOGGER.setLevel(logging.getLevelName(logging_level))
    handler.setLevel(logging_level)
    LOGGER.addHandler(handler)

    APP.run()  # pragma: no cover
