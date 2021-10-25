import os
from unittest import TestCase
from dienna.auth import AuthenticationManager
import logging

logging.basicConfig(level=logging.DEBUG)


class TestSSO(TestCase):

    def test_login(self):
        am = AuthenticationManager()
        status, session = am.get_session(os.environ['SSO_USER'], os.environ['SSO_PASS'])
        resp = session.get(
            'https://office.kemenkeu.go.id/api/AmplopNd',
            params={'urgensi': 'All', 'reset': 'false', 'tagnd': 'All', 'limit': '1', 'offset': '0'}
        )
        self.assertTrue(resp.json()['totalItems'] >= 0)
        am.logout()
