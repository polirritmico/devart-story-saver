#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os


class Credentials:
    api_name: str
    raw_credentials: dict[str, str]

    def __init__(self, api_name: str):
        self.api_name = api_name

    def load_credentials(self, filename: str) -> json:
        if not isinstance(filename, str) or filename == "":
            raise ValueError("Input filename must be a non-empty string.")
        try:
            with open(os.path.abspath(filename), "r", encoding="utf-8") as stream:
                credentials = json.load(stream)
        except Exception as error:
            raise IOError(f"Error reading the file {filename}") from error

        self.raw_credentials = credentials
        for key, value in credentials.items():
            setattr(self, key, value)
        return self.raw_credentials
