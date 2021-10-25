import os
import unittest
from dienna.auth import AuthenticationManager
from dienna.nadine import Nadine
import logging

logging.basicConfig(level=logging.DEBUG)


class TestSSO(unittest.TestCase):

    def test_login(self):
        am = AuthenticationManager()
        status, session = am.get_session(os.environ['SSO_USER'], os.environ['SSO_PASS'])
        resp = session.get(
            'https://office.kemenkeu.go.id/api/AmplopNd',
            params={'urgensi': 'All', 'reset': 'false', 'tagnd': 'All', 'limit': '1', 'offset': '0'}
        )
        self.assertTrue(resp.json()['totalItems'] >= 0)
        am.logout()
        return am


class TestNadine(unittest.TestCase):

    def setUp(self) -> None:
        self.am = AuthenticationManager()
        status, session = self.am.get_session(os.environ['SSO_USER'], os.environ['SSO_PASS'])
        self.nadine = Nadine(session=session)

    def test_mejaku(self):
        resp = self.nadine.get_mejaku(limit=15)
        print(resp)

    def tearDown(self) -> None:
        self.am.logout()


if __name__ == '__main__':
    unittest.main()
