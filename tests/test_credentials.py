#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

import pytest

from src.credentials import Credentials


def test_load_file() -> None:
    file = "tests/files/credentials.json"
    expected = {
        "client_id": "123456",
        "client_secret": "aSecret_pass",
    }
    credentials = Credentials("deviantart")
    credentials.load_credentials(file)

    assert len(credentials.raw_credentials) == len(expected)
    assert credentials.client_id == expected["client_id"]
    assert credentials.client_secret == expected["client_secret"]


def test_load_bad_file() -> None:
    file = "bad_file"
    expected_error = "error reading"
    credentials = Credentials("deviantart")
    with pytest.raises(IOError) as error:
        credentials.load_credentials(file)
    output_error = error.value.args[0].lower()
    assert expected_error in output_error


def test_generate_key() -> None:
    credentials = Credentials("mock")
    output = credentials.generate_new_token_key()
    assert isinstance(output, bytes)
    base64.urlsafe_b64decode(output)
