import logging
import requests
from bs4 import BeautifulSoup as Bs


class AuthenticationManager(object):
    """
    Object untuk manage SSO Auth
    """

    def __init__(self):
        logging.debug("Session init")
        self.__session = requests.session()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/94.0.4606.81 Safari/537.36'
        }

    def get_oauth_data(self):
        resp = self.__session.get('https://office.kemenkeu.go.id/index/index')
        soup = Bs(resp.content, 'html5lib')
        return soup.form.get('action'), {
            i.get('name'): i.get('value') for i in soup.form.find_all('input') if i.get('name') is not None
        }

    def connect_authorize(self, url, data):
        resp = self.__session.post(
            url,
            data=data
        )
        soup = Bs(resp.content, 'html5lib')
        return resp.url, {i.get('name'): i.get('value') for i in soup.form.find_all('input')}

    def login(self, url, data, username, password):
        form_data = data
        form_data.update({
            'Username': username,
            'Password': password,
            'button': 'login',
        })

        resp = self.__session.post(
            url,
            data=form_data
        )
        soup = Bs(resp.content, 'html5lib')
        return soup.form.get('action'), {i.get('name'): i.get('value') for i in soup.form.find_all('input')}

    def sign_in_oidc(self, url, data):
        resp = self.__session.post(
            url,
            data=data
        )

        return resp.url == 'https://office.kemenkeu.go.id/home'

    def logout(self):
        resp = self.__session.get('https://office.kemenkeu.go.id/Index/Logout')
        soup = Bs(resp.content, 'html5lib')

        self.__session.post(
            soup.form.get('action'),
            data={i.get('name'): i.get('value') for i in soup.form.find_all('input')}
        )

    def get_session(self, username, password):
        logging.debug("Get session")

        url, oauth_data = self.get_oauth_data()
        logging.debug("Get oauth data {} {}".format(url, oauth_data))

        url, auth_data = self.connect_authorize(url, oauth_data)
        logging.debug("Get auth data {} {}".format(url, oauth_data))

        url, login_data = self.login(url, auth_data, username, password)
        logging.debug("Get login data {} {}".format(url, login_data))

        status = self.sign_in_oidc(url, login_data)
        logging.debug("Login status {}".format(status))

        return status, self.__session

    def __del__(self):
        if self.__session:
            self.__session.close()
            del self.__session
