import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online interessante para
        # listas de tarefas. Ela decide verificar sua home page
        self.browser.get('http://localhost:8000')

        # Ela percebe que o titulo da pagína e o cabeçalho mencionam listas de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela digita "Buy peacock feathers" em uma caixa de texto
        # (o hobby de Edith é fazer iscas para pesca com fly)
        inputbox.send_keys('Buy peacock feathers')

        # Quando ela tecla enter, a pagína é atualizada
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # e agora a página lista
        # 1: Buy peacock feathers" como um item em uma lista de tarefas
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item
        # Ela insere "Use peacock feathers to make a fly"

        # A pagína e atualizada novamente e agora mostra os dois itens em sua lista

        # Edith se pergunta se o site lembrará de sua lista.
        # Então ela nota que o site gerou um URL unico para ela --há um pequeno texto explicativo para isso

        # Ela acessa esse URL - sua lista de tarefas continua lá

        # Satisfeita, ela volta a dormir

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
