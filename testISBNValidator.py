from ISBNValidator import ISBNValidator
import unittest


class testISBNValidator(unittest.TestCase):

    def testIsValid(self):
        testISBNValidator.testISBN10Valid(self)
        testISBNValidator.testISBN13Valid(self)

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

    def testConvertToISBN13(self):
        self.assertEqual(ISBNValidator.convertToISBN13('85-359-0277-5'), '978-85-359-0277-8')
        self.assertEqual(ISBNValidator.convertToISBN13('0-8044-2957-X'), '978-0-8044-2957-3')
        self.assertEqual(ISBNValidator.convertToISBN13('080442957X'), '9780804429573')

    def testConvertToISBN13NotValid(self):
        self.assertFalse(ISBNValidator.convertToISBN13('85-359-0277-4'))

    def testConvertToISBN10(self):
        self.assertFalse(ISBNValidator.convertToISBN10('978-0-8044-2957-3'), '0-8044-2957-X')
        self.assertFalse(ISBNValidator.convertToISBN10('9780804429573'), '080442957X')
        self.assertFalse(ISBNValidator.convertToISBN10('978-85-359-0277-8'), '85-359-0277-5')

    def testConvertToISBN10NotValid(self):
        self.assertFalse(ISBNValidator.convertToISBN10('978-85-359-0277-7'))
