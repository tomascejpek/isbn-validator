from ISBNValidator import ISBNValidator
import unittest


class testISBNValidator(unittest.TestCase):
    def testISBN10Valid(self):
        self.assertTrue(ISBNValidator.isValidISBN10('9971-5-0210-0'))
        self.assertTrue(ISBNValidator.isValidISBN10('9971502100'))
        self.assertTrue(ISBNValidator.isValidISBN10('85-359-0277-5'))
        self.assertTrue(ISBNValidator.isValidISBN10('0-8044-2957-X'))
        self.assertTrue(ISBNValidator.isValidISBN10('0-8044-2957-x'))

    def testISBN10NotValid(self):
        self.assertFalse(ISBNValidator.isValidISBN10('08-0442-9-57x'))
        self.assertFalse(ISBNValidator.isValidISBN10('1234567891'))
        self.assertFalse(ISBNValidator.isValidISBN10('123'))

    def testISBN13Valid(self):
        self.assertTrue(ISBNValidator.isValidISBN13('978-80-755-5124-5'))
        self.assertTrue(ISBNValidator.isValidISBN13('9788088268444'))

    def testISBN13NotValid(self):
        self.assertFalse(ISBNValidator.isValidISBN13('978-80-75-5512-45'))
