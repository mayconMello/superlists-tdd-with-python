from django.conf import settings
from django.contrib.auth import get_user_model

from functional_tests.server_tools import create_session_on_server
from functional_tests.management.commands.create_session import create_pre_authenticated_session
from functional_tests.base import FunctionalTest

User = get_user_model()


class MyListTest(FunctionalTest):
    def create_pre_authenticated_session(self, email):
        if self.staging_server:
            session_key = create_session_on_server(self.staging_server, email)
        else:
            session_key = create_pre_authenticated_session(email)

        # para definir um cookie, precisamos antes acessar o dominio.
        # as paginas 404 são as que carregam mais rapidamente!
        self.browser.get(f'{self.live_server_url}/404_no_such_url/')
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/'
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_out(email)

        # Edith é uma usuária logada
        self.create_pre_authenticated_session(email)
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_in(email)
