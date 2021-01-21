import os
import poplib
import re
import time
from django.core import mail

from selenium.webdriver.common.keys import Keys
import re

from superlists.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
from functional_tests.base import FunctionalTest

TEST_EMAIL = 'edith@example.com'

SUBJECT = 'Your login link for Superlists'


class LoginTest(FunctionalTest):

    def test_can_get_email_link_to_log_in(self):
        # Edith acessa o incrível site de superlistas
        # e, pela primeira vez, percebe que há uma seção de "Log In" na barra
        # de navegação. Essa seção está lhe dizendo para inserir seu endereço de email
        # portanto ela faz isso
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # Uma mensagem aparece informando lhe que um email foi enviado
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # Ela verifica seu email e encontra uma mensagem
        email = mail.outbox[0]
        self.assertIn(TEST_EMAIL, email.to)
        self.assertEqual(email.subject, SUBJECT)
        body = self.wait_for_email(TEST_EMAIL, SUBJECT)

        # A mensagem contém um link com um url
        self.assertIn('Use this link to log in', body)
        url_search = re.search(r'http://.+/.+$', body)

        if not url_search:
            self.fail(f'Could not find url in email body:\n{body}')

        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # Ela clica no url
        self.browser.get(url)

        # Ela está logada!
        self.wait_to_be_logged_in(TEST_EMAIL)

        # Agora ela faz logout
        self.browser.find_element_by_link_text('Log out').click()

        # Ela não está mais logada!
        self.wait_to_be_logged_out(TEST_EMAIL)

    def wait_for_email(self, test_email, subject):
        if not self.staging_server:
            email = mail.outbox[0]
            self.assertIn(test_email, email.to)
            self.assertEqual(email.subject, subject)
            return email.body

        email_id = None
        start = time.time()
        inbox = poplib.POP3_SSL('pop3.mailtrap.io')
        try:
            inbox.user(EMAIL_HOST_USER)
            inbox.pass_(EMAIL_HOST_PASSWORD)
            while time.time() - start < 60:
                count, _ = inbox.stat()
                for i in reversed(range(max(1, count - 10), count + 1)):
                    print('getting msg', i)

                    _, lines, __ = inbox.retr(i)
                    lines = [l.decode('utf-8') for l in lines]
                    print(lines)
                    if f'Subject: {subject}' in lines:
                        email_id = i
                        body = '\n'.join(lines)
                        return body

                time.sleep(5)
        finally:
            if email_id:
                inbox.dele(email_id)

            inbox.quit()
