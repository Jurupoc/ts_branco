from src.negocio.Cliente import Cliente

import unittest


class TestClienteCpf(unittest.TestCase):
    def test_cliente_cpf(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_cpf(), "12345678900", msg= "O CPF do cliente deveria ser 12345678900")


class TestClienteNome(unittest.TestCase):
    def test_cliente_nome(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_nome(), "João", msg= "O nome do cliente deveria ser João")


class TestClienteContas(unittest.TestCase):
    def test_cliente_contas(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_contas(), [], msg= "O cliente não deveria possuir contas")


class TestClienteAdicionarConta(unittest.TestCase):
    def test_cliente_adicionar_conta(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        self.assertEqual(cliente.get_contas(), ["123"], msg= "O cliente deveria possuir a conta 123")


class TestClienteRemoverConta(unittest.TestCase):
    def test_cliente_remover_conta(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        cliente.remover_conta("123")
        self.assertEqual(cliente.get_contas(), [], msg= "O cliente não deveria possuir contas")


class TestClienteRemoverTodasAsContas(unittest.TestCase):
    def test_cliente_remover_todas_as_contas(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        cliente.adicionar_conta("456")
        cliente.remover_todas_as_contas()
        self.assertEqual(cliente.get_contas(), [], msg= "O cliente não deveria possuir contas")


def run_cliente_tests() -> None:
    suite =        unittest.defaultTestLoader.loadTestsFromTestCase(TestClienteCpf)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestClienteNome))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestClienteContas))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestClienteAdicionarConta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestClienteRemoverConta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestClienteRemoverTodasAsContas))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    run_cliente_tests()
