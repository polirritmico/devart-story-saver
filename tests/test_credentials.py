#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from src.credentials import Credentials


def test_load_file() -> None:
    file = "tests/credentials.json"
    expected = {
        "client_id": "123456",
        "client_secret": "aSecret_pass",
    }
    credentials = Credentials("deviantart")
    output = credentials.load_credentials(file)
    assert len(output) == len(expected)
    for item, value in expected.items():
        assert item in output
        assert output[item] == value
