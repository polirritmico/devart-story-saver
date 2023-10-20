#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os


class Credentials:
    client_id: str
    client_secret: str
    secrets_file: str
    api_name: str

    def __init__(self, api_name: str):
        self.api_name = api_name

    def load_credentials(self, filename: str):
        if not isinstance(filename, str) or filename == "":
            raise ValueError("Input filename must be a non-empty string.")
        try:
            with open(os.path.abspath(filename), "r", encoding="utf-8") as stream:
                credentials = json.load(stream)
        except IOError as error:
            raise Exception(f"Error reading the file {filename}") from error
