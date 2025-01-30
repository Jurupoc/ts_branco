from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.negocio.ContaEspecial import ContaEspecial

import unittest


class TestContaEspecial(unittest.TestCase):
    def setUp(self):
        self.conta = ContaEspecial("12345", 100.0)

    def test_getters_and_setters(self):
        self.assertEqual(self.conta.getBonus(), 0.0)

        self.conta.setBonus(50.0)
        self.assertEqual(self.conta.getBonus(), 50.0)

    def test_creditar(self):
        self.conta.creditar(200.0)
        self.assertEqual(self.conta.getSaldo(), 300.0)  # 100 + 200
        self.assertEqual(self.conta.getBonus(), 2.0)  # 1% de 200

    def test_renderbonus(self):
        self.conta.setBonus(10.0)
        self.conta.renderbonus()
        self.assertEqual(self.conta.getSaldo(), 110.0)  # 100 + 10
        self.assertEqual(self.conta.getBonus(), 0.0)

    def test_get_tipo(self):
        self.assertEqual(self.conta.get_tipo(), "especial")


def runContaEspecialTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestContaEspecial)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runContaEspecialTests()
