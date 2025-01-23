import unittest

from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB

from src.negocio.Banco import Banco
from src.negocio.Cliente import Cliente
from src.negocio.Conta import Conta


class TesteBanco(unittest.TestCase):
    def setUp(self):
        self.cliente_db_conn = RepositorioClientesArquivoDB()
        self.conta_db_conn = RepositorioContasArquivoDB()
        self.banco = Banco(self.cliente_db_conn, self.conta_db_conn)

    def test_cadastrar_cliente(self):
        teste_cpf: string = "123.456.789-00"
        teste_nome: string = "Gabriel"
        cliente_teste: Cliente = Cliente(teste_nome, teste_cpf)

        self.banco.cadastrar_cliente(cliente_teste)

        resultado = self.banco.procurar_cliente(teste_cpf)
        self.assertEqual(resultado, cliente_teste)

        self.banco.remover_cliente(teste_cpf)

        resultado = self.banco.procurar_cliente(teste_cpf)
        self.assertIsNone(resultado)

def run_banco_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TesteBanco)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    run_banco_tests()
