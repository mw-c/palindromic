import palindromic
import unittest
import StringIO

class Test_is_palindromic(unittest.TestCase):

    def test_true(self):
        self.assertTrue(palindromic.is_palindromic([1,2,2,1]))

    def test_false(self):
        self.assertFalse(palindromic.is_palindromic([1,2,3,1]))

    def test_empty(self):
        self.assertFalse(palindromic.is_palindromic([]))

class Test_base10_to_baseN(unittest.TestCase):

    def test_0_in_base2(self):
        result = palindromic.base10_to_baseN(0, 2)
        self.assertEqual(result, [0])

    def test_17_in_base2(self):
        result = palindromic.base10_to_baseN(17, 2)
        self.assertEqual(result, [1, 0, 0, 0, 1])

    def test_7_in_base10(self):
        result = palindromic.base10_to_baseN(7, 10)
        self.assertEqual(result, [7])

    def test_16_in_base3(self):
        result = palindromic.base10_to_baseN(16, 3)
        self.assertEqual(result, [1, 2, 1])

    def test_997_in_base996(self):
        result = palindromic.base10_to_baseN(997, 996)
        self.assertEqual(result, [1, 1])

class Test_find_min_base_palindromic(unittest.TestCase):

    def test_17(self):
        result = palindromic.find_min_base_palindromic(17)
        self.assertEqual(result, 2)

    def test_16(self):
        result = palindromic.find_min_base_palindromic(16)
        self.assertEqual(result, 3)

    def test_997(self):
        result = palindromic.find_min_base_palindromic(997)
        self.assertEqual(result, 996)

    def test_0(self):
        result = palindromic.find_min_base_palindromic(0)
        self.assertEqual(result, 2)

class Test_output_to_file(unittest.TestCase):

    def test(self):
        file = StringIO.StringIO()
        data = [(1000,9)]
        palindromic.output_to_file(data, file)
        self.assertEqual(file.getvalue().strip(), "1000,9")


if __name__ == '__main__':
    unittest.main()