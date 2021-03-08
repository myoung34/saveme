# -*- coding: utf-8 -*-
""" Test fixtures """
import json
import os

import pytest


@pytest.fixture()
def api_gateway_push_event():
    PAYLOAD_FILE = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'api_gateway_push_event.json'
    )
    with open(PAYLOAD_FILE) as data_file:
        return json.load(data_file)


@pytest.fixture()
def kinesis_get_record():
    PAYLOAD_FILE = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'kinesis_get_record.json'
    )
    with open(PAYLOAD_FILE) as data_file:
        return json.load(data_file)
