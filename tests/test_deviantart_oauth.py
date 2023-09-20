#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from src.deviantart_oauth import DeviantartOauth


def test_oauth() -> None:
    client_id = ""
    client_secret = ""
    client = DeviantartOauth(client_id, client_secret)
    output = client.request_user_auth()
