import unittest
from funcionario import Funcionario
from unittest.mock import patch # decorador ou context manager

class TestFuncionario(unittest.TestCase):

    # antes de tudo
    @classmethod
    def setUpClass(cls):
        print('***********setUpClass***********')

    # depois de tudo
    @classmethod
    def tearDownClass(cls):
        print('***********tearDownClass***********')

    # roda antes de cada teste
    def setUp(self):
        self.ana = Funcionario('Ana', 'Silva', 5000)
        self.pedro = Funcionario('Pedro', 'Gomes', 4000)
        print('**********setUp**********')

    # roda depois de cada teste
    def tearDown(self):
        print('**********tearDown**********')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.ana.email, 'ana.silva@email.com')
        self.assertEqual(self.pedro.email, 'pedro.gomes@email.com')

        self.ana.nome = 'Aninha'
        self.pedro.sobrenome = 'Freire'

        self.assertEqual(self.ana.email, 'aninha.silva@email.com')
        self.assertEqual(self.pedro.email, 'pedro.freire@email.com')

    def test_nome_completo(self):
        print('test_nome_completo')
        self.assertEqual(self.ana.nome_completo, 'Ana Silva')
        self.assertEqual(self.pedro.nome_completo, 'Pedro Gomes')

        self.ana.nome = 'Aninha'
        self.pedro.sobrenome = 'Freire'

        self.assertEqual(self.ana.nome_completo, 'Aninha Silva')
        self.assertEqual(self.pedro.nome_completo, 'Pedro Freire')

    def test_aplica_aumento(self):
        print('test_aplica_aumento')
        self.ana.aplica_aumento()
        self.pedro.aplica_aumento()

        self.assertEqual(self.ana.salario, 5500)
        self.assertEqual(self.pedro.salario, 4400)

    def test_pagina(self):
        print('test_pagina')
        with patch('funcionario.requests.get') as get_simulado:
            get_simulado.return_value.ok = True
            get_simulado.return_value.text = 'Sucesso'

            pagina_ana = self.ana.pagina()
            get_simulado.assert_called_with('https://empresa.com/ana-silva')

            self.assertEqual(pagina_ana, 'Sucesso')

            ###

            get_simulado.return_value.ok = False

            pagina_ana = self.ana.pagina()
            get_simulado.assert_called_with('https://empresa.com/ana-silva')

            self.assertEqual(pagina_ana, 'Má requisição!')


if __name__ == '__main__':
    unittest.main()
