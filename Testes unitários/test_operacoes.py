import unittest
from operacoes import divide, multiplica, subtrai, area_circulo
from math import pi

class TestOperacoes(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(8,4), 2)
        self.assertEqual(divide(-1,-1), 1)
        self.assertEqual(divide(-10,5), -2)
        self.assertEqual(divide(3,2), 1.5)
        self.assertAlmostEqual(divide(10,3), 10/3)

        # duas formas de testar o raise
        with self.assertRaises(ZeroDivisionError):
            divide(2,0)
        #self.assertRaises(ZeroDivisionError, divide, 2,0)

    def test_multiplica(self):
        self.assertEqual(multiplica(8,4), 32)
        self.assertEqual(multiplica(-1,-1), 1)
        self.assertEqual(multiplica(-10,5), -50)

    def test_subtrai(self):
        self.assertEqual(subtrai(8,4), 4)
        self.assertEqual(subtrai(-1,-1), 0)
        self.assertEqual(subtrai(-10,5), -15)

    def test_area_circulo(self):
        self.assertEqual(area_circulo(1), pi)
        self.assertEqual(area_circulo(0), 0)
        self.assertEqual(area_circulo(3), pi*(3**2))

        # duas formas de testar o raise
        with self.assertRaises(ValueError):
            area_circulo(-2)
        # self.assertRaises(ValueError, area_circulo, -2)

# python -m unittest test_operacoes.py
if __name__ == '__main__':
    unittest.main()
