#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauthlib.oauth2 import Client

from src.oauth import DeviantArtOauth


class Deviantart:
    """
    Docs: https://www.deviantart.com/developers/authentication
    """

    oauth: DeviantArtOauth

    def __init__(self, client_id: str, client_secret: str):
        self.oauth = DeviantArtOauth(
            client_id,
            client_secret,
            "https://polirritmico.github.io/devart-story-saver/oauth-redirect.html",
        )

    def request_user_auth(self):
        endpoint = "/oauth2/authorize"
        client_id = ""
        client = Client(client_id, token_type="Bearer")
        uri = self.base_url + endpoint
        token = client.add_token(uri, http_method="GET")
        print(token)
