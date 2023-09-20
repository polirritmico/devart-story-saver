#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauthlib.oauth2 import Client


class DeviantartOauth:
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
        """Requests user authourization code grant.

        Before making the API calls for a user, you must ask that user to
        authorize the application. First you should redirect the user to
        DeviantArt's authorization URL along with the required query-string
        parameters below.

        API Args:
            response_type (string): Required. Setting response_type to code is
                required.
            client_id (int): Required. Your app's client_id (obtained during
                app registration)
            redirect_uri (string) : Required. Your app's URI which the user
                should be redirected to after authorizing. This redirect_uri
                MUST be in your apps redirect uri whitelist, non-whitelisted
                uris will be rejected.
            scope (string): Optional. The scope you wish to access (space
                separated), defaults to basic.
            state (string) : Optional. state will be sent back as part of the
                redirect_uri query paramerters, this should be a unique
                identifer you create to verify the redirect is coming from your
                original request see http://tools.ietf.org/html/rfc6749#section-10.12.

        """
        endpoint = "/oauth2/authorize"
        client_id = ""
        client = Client(client_id, token_type="Bearer")
        uri = self.base_url + endpoint
        token = client.add_token(uri, http_method="GET")
        print(token)
