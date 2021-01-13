from functional_tests.base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a pagina inicial e acidentalmente tenta submeter
        # um item vazio na lista. Ela tecla Enter na caixa de entrada

        # A pagina inicial é atualizada e ha uma mensagem de erro informando
        # que itens da lista não podem estar em branco

        # Ela tenta novamwente com um texto para o item, e isso agora funciona

        # De forma perversa, ela agora decide submeter um segundo item em
        # branco na lista

        # Ela recebe um aviso semelhante na pagina da lista

        # E ela pode corrigir isso preenchendo o item com um texto
        self.fail('write me')
