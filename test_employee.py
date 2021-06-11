import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        print('\ntest_email')

        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue','Smith',60000)

        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')

        emp_1.first = 'Josh'
        emp_2.last = 'Jabberwocky'

        self.assertEqual(emp_1.email, 'Josh.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Jabberwocky@email.com')

    def test_fullname(self):
        print('\ntest_fullname')

        emp_1 = Employee('Josiah', 'Mask', 50000)
        emp_2 = Employee('Ricky', 'Smith', 50000)

        self.assertEqual(emp_1.fullname, 'Josiah Mask')
        self.assertEqual(emp_2.fullname, 'Ricky Smith')

        emp_1.first = 'Cris'
        emp_2.last = 'Morty'

        self.assertEqual(emp_1.fullname, 'Cris Mask')
        self.assertEqual(emp_2.fullname, 'Ricky Morty')

    def test_apply_raise(self):
        print('\ntest_apply_raise')

        emp_1 = Employee('Sitama', 'Genos', 100)
        emp_2 = Employee('Tanjiro', 'Gintama', 100000)

        self.assertEqual(emp_1.pay, 100)
        self.assertEqual(emp_2.pay, 100000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 105)
        self.assertEqual(emp_2.pay, 105000)





if __name__ == '__main__':
    unittest.main()