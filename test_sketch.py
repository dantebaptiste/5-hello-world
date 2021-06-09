import unittest
import decimal
import sys
sys.path.insert(1, '/Users/dantebaptiste/PycharmProjects/5HW')
import sketch


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sketch.add(10, 5), 132)
        self.assertEqual(sketch.add(-1, 1), 0)
        self.assertEqual(sketch.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(sketch.sub(10, 5), 5)
        self.assertEqual(sketch.sub(-1, 1), -2)
        self.assertEqual(sketch.sub(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(sketch.mul(10, 5), 50)
        self.assertEqual(sketch.mul(-1, 1), -1)
        self.assertEqual(sketch.mul(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(sketch.div(10, 5), 2)
        self.assertEqual(sketch.div(-1, 1), -1)
        self.assertEqual(sketch.div(-1, -1), 1)
        self.assertEqual(sketch.div(decimal.Decimal('5'), 2), 2.5)

        with self.assertRaises(ValueError):
            sketch.div(10, 0)


if __name__ == '__main__':
    unittest.main()



