from src.negocio.Cliente import Cliente
from src.exceptions.ClienteJaPossuiContaException import ClienteJaPossuiContaException
from src.exceptions.ClienteNaoPossuiContaException import ClienteNaoPossuiContaException


import unittest


class TestsCliente(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("João Silva", "123.456.789-00")

    def test_getters_and_setters(self):
        self.assertEqual(self.cliente.get_nome(), "João Silva")
        self.assertEqual(self.cliente.get_cpf(), "123.456.789-00")

        self.cliente.set_nome("Maria Souza")
        self.cliente.set_cpf("987.654.321-00")

        self.assertEqual(self.cliente.get_nome(), "Maria Souza")
        self.assertEqual(self.cliente.get_cpf(), "987.654.321-00")

    def test_adicionar_conta(self):
        self.cliente.adicionar_conta("1234")
        self.assertIn("1234", self.cliente.get_contas())

        with self.assertRaises(ClienteJaPossuiContaException):
            self.cliente.adicionar_conta("1234")  # Conta já existente

    def test_remover_conta(self):
        self.cliente.adicionar_conta("5678")
        self.cliente.remover_conta("5678")
        self.assertNotIn("5678", self.cliente.get_contas())

        with self.assertRaises(ClienteNaoPossuiContaException):
            self.cliente.remover_conta("5678")  # Conta inexistente

    def test_remover_todas_as_contas(self):
        self.cliente.adicionar_conta("1111")
        self.cliente.adicionar_conta("2222")
        self.cliente.remover_todas_as_contas()
        self.assertEqual(len(self.cliente.get_contas()), 0)

    def test_procurar_conta(self):
        self.cliente.adicionar_conta("3333")
        self.assertEqual(self.cliente.procurar_conta("3333"), 0)
        self.assertEqual(self.cliente.procurar_conta("9999"), -1)

    def test_consultar_numero_conta(self):
        self.cliente.adicionar_conta("4444")
        self.assertEqual(self.cliente.consultar_numero_conta(0), "4444")

    def test_equals(self):
        outro_cliente = Cliente("Carlos Silva", "123.456.789-00")
        cliente_diferente = Cliente("Ana Lima", "000.111.222-33")

        self.assertEqual(self.cliente, outro_cliente)
        self.assertNotEqual(self.cliente, cliente_diferente)
        self.assertNotEqual(self.cliente, "String qualquer")  # Comparação com objeto diferente

    def test_str(self):
        self.cliente.adicionar_conta("5555")
        esperado = "Nome: João Silva\nCPF: 123.456.789-00\nContas: ['5555']"
        self.assertEqual(str(self.cliente), esperado)


def run_cliente_tests() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestsCliente)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    run_cliente_tests()

