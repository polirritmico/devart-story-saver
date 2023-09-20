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
        metadata = {}
        for key, value in response.__dict__.items():
            if key.startswith("_"):
                continue
            metadata[key] = value
        response_with_metadata = response.json()
        response_with_metadata["metadata"] = metadata
        return response_with_metadata

    def get(self, url: str = "") -> dict:
        self._check_headers()
        full_url = self._make_full_url(url)
        response = requests.get(
            url=full_url, headers=self.headers, timeout=self.time_out_seconds
        )
        return response.json()

    def post(
        self, url: str = "", data: Optional[Dict] = None, auth: Optional[Tuple] = None
    ) -> dict:
        self._check_headers()
        full_url = self._make_full_url(url)
        response = requests.post(
            url=full_url,
            data=json.dumps(data),
            auth=auth,
            headers=self.headers,
            timeout=self.time_out_seconds,
            verify=self.verify,
        )
        response_with_metadata = self.collect_response_metadata(response)
        return response_with_metadata

    def set_headers(self, **headers) -> dict:
        if len(headers) == 0:
            raise ValueError("Got empty data to build the header.")
        self.headers = {}
        for key, value in headers.items():
            self.headers[key] = value
        return self.headers

    def _check_headers(self) -> None:
        if not hasattr(self, "headers") or self.headers is None or self.headers == {}:
            msg = "Missing headers. Try set_headers(headers) before the API call."
            raise ValueError(msg)

    def _make_full_url(self, endpoint: str) -> str:
        not_a_full_url = not endpoint.startswith("http")
        if not_a_full_url and self.base_url == "":
            raise ValueError("Could not execute the API requests without a full url.")
        if not_a_full_url:
            endpoint = self.base_url + endpoint
        return endpoint
