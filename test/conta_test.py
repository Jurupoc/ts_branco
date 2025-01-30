import unittest
from src.negocio.Conta import Conta
from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException


class TestConta(unittest.TestCase):
    def setUp(self):
        self.conta = Conta("12345", 100.0)

    def test_getters_and_setters(self):
        self.assertEqual(self.conta.getNumero(), "12345")
        self.assertEqual(self.conta.getSaldo(), 100.0)

        self.conta.setNumero("67890")
        self.conta.setSaldo(200.0)

        self.assertEqual(self.conta.getNumero(), "67890")
        self.assertEqual(self.conta.getSaldo(), 200.0)

    def test_creditar(self):
        self.conta.creditar(50.0)
        self.assertEqual(self.conta.getSaldo(), 150.0)

    def test_debitar(self):
        self.conta.debitar(30.0)
        self.assertEqual(self.conta.getSaldo(), 70.0)

        with self.assertRaises(SaldoInsuficienteException):
            self.conta.debitar(200.0)

    def test_get_tipo(self):
        self.assertEqual(self.conta.get_tipo(), "normal")

    def test_equals(self):
        outra_conta = Conta("12345", 50.0)
        conta_diferente = Conta("99999", 50.0)

        self.assertEqual(self.conta, outra_conta)
        self.assertNotEqual(self.conta, conta_diferente)
        self.assertNotEqual(self.conta, "string qualquer")


def runContaTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestConta)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runContaTests()