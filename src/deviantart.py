#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauthlib.oauth2 import Client


class Deviantart:
    """
    Docs: https://www.deviantart.com/developers/authentication
    """

    base_url = "https://www.deviantart.com"
    client_id: str
    client_secret: str

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def request_user_auth(self):
        endpoint = "/oauth2/authorize"
        client_id = ""
        client = Client(client_id, token_type="Bearer")
        uri = self.base_url + endpoint
        token = client.add_token(uri, http_method="GET")
        print(token)
