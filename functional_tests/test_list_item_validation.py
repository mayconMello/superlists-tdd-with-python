from selenium.webdriver.common.keys import Keys
from functional_tests.base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a pagina inicial e acidentalmente tenta submeter
        # um item vazio na lista. Ela tecla Enter na caixa de entrada
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        # A pagina inicial é atualizada e ha uma mensagem de erro informando
        # que itens da lista não podem estar em branco
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
            )
        )

        # Ela tenta novamwente com um texto para o item, e isso agora funciona
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # De forma perversa, ela agora decide submeter um segundo item em
        # branco na lista
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Ela recebe um aviso semelhante na pagina da lista
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
            )
        )

        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        # E ela pode corrigir isso preenchendo o item com um texto
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

