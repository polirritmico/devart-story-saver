#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

from cryptography.fernet import Fernet


class Credentials:
    api_name: str
    raw_credentials: dict[str, str]
    token_vault_key: str
    # encoded_token: str

    def __init__(self, api_name: str):
        self.api_name = api_name

    def generate_new_token_key(self) -> str:
        return Fernet.generate_key()

    def decrypt(self, encrypted: str) -> str:
        self._check_token_vault_key()
        fernet = Fernet(self.token_vault_key.encode())
        decrypted = fernet.decrypt(encrypted.encode())
        return decrypted.decode()

    def encrypt(self, string: str) -> str:
        self._check_token_vault_key()
        fernet = Fernet(self.token_vault_key.encode())
        encrypted = fernet.encrypt(string.encode())
        return encrypted.decode()

    def _check_token_vault_key(self) -> None:
        if self.token_vault_key is None or self.token_vault_key == "":
            raise ValueError("Missing token vault key. Try load_credentials()")

    def load_credentials(self, filename: str) -> json:
        if not isinstance(filename, str) or filename == "":
            raise ValueError("Input filename must be a non-empty string.")
        try:
            with open(os.path.abspath(filename), "r", encoding="utf-8") as stream:
                self.raw_credentials = json.load(stream)
        except Exception as error:
            raise IOError(f"Error reading the file {filename}") from error

        for key, value in self.raw_credentials.items():
            setattr(self, key, value)
        return self.raw_credentials

    def store_token(self, token, store_path: str) -> None:
        with open(store_path, "w", encoding="utf-8") as stream:
            stream.write(token)
