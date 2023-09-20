#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.api_connector import ApiConnector


def test_api_connector_headers_validations() -> None:
    api = ApiConnector()
    with pytest.raises(ValueError) as error:
        api._check_headers()
    expected = "missing headers"
    output_error = str(error.value.args[0]).lower()

    assert expected in output_error


def test_api_connector_make_full_url() -> None:
    api = ApiConnector()
    api.base_url = "https://test_url.org"
    endpoint = "/endpoint"
    expected = "https://test_url.org/endpoint"
    output = api._make_full_url(endpoint)

    assert expected == output


def test_api_connector_make_error_full_url() -> None:
    api = ApiConnector()
    api.base_url = ""
    with pytest.raises(ValueError) as error:
        api._make_full_url("/endpoint")
    expected = "without a full url"
    output_error = str(error.valur.args[0]).lower()

    assert expected in output_error
