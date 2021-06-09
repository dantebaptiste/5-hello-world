import unittest
import sys
#sys.path.insert(1, '/5HW')
import sketch


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = sketch.add(10, 5)
        self.assertEqual(result, 15)




