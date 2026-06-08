import unittest
from calcolatrice import somma, sottrazione, moltiplicazione, divisione

class TestCalcolatrice(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 2

    def tearDown(self):
        pass

    def test_somma(self):
        self.assertEqual(somma(self.a, self.b), 12)

    def test_sottrazione(self):
        self.assertEqual(sottrazione(self.a, self.b), 8)

    def test_moltiplicazione(self):
        self.assertEqual(moltiplicazione(self.a, self.b), 20)

    def test_divisione(self):
        self.assertEqual(divisione(self.a, self.b), 5)

    def test_divisione_per_zero(self):
        with self.assertRaises(ValueError):
            divisione(self.a, 0)


class TestCalcolatriceSetUpClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nInizio test suite")
        cls.valori = (10, 2)

    @classmethod
    def tearDownClass(cls):
        print("\nFine test suite")

    def test_somma_con_classe(self):
        self.assertEqual(somma(*self.valori), 12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
