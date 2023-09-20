#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Dict, Optional, Tuple

import requests


class ApiConnector:
    base_url: str
    headers: dict
    body: dict
    time_out_seconds: float = 5
    verify: bool = True

    def collect_response_metadata(self, response: requests.Response) -> dict:
        pass

    def get(self, url: str = "") -> dict:
        pass

    def post(
        self, url: str = "", data: Optional[Dict] = None, auth: Optional[Tuple] = None
    ) -> dict:
        pass

    def set_headers(self, **headers) -> dict:
        pass

    def _check_headers(self) -> None:
        pass

    def _make_full_url(self, endpoint: str) -> str:
        pass
