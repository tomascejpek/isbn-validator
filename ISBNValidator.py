import re


class ISBNValidator:

    @staticmethod
    def isValid(code):
        return ISBNValidator.isValidISBN10(code) or ISBNValidator.isValidISBN13(code)

    @staticmethod
    def isValidISBN10(code):
        ISBN10_REGEX = "^(?:(\d{9}[0-9Xx])|(?:(\d{1,5})(?:-|\s)(\d{1,7})(?:-|\s)(\d{1,6})(?:-|\s)([0-9Xx])))$"
        ISBN10_NUMBER = "[\dXx]"
        matcher = re.search(ISBN10_REGEX, code)
        if matcher is None:
            return False
        code = ''.join(re.findall(ISBN10_NUMBER, code))
        sum = 0
        for i in range(1, 11):
            sum += i * int(10 if code[10 - i] in ['X', 'x'] else code[10 - i])
        if sum % 11 == 0:
            return True
        return False

    @staticmethod
    def isValidISBN13(code):
        ISBN13_REGEX = "^(978|979)(?:(\d{10})|(?:(?:-|\s)(\d{1,5})(?:-|\s)(\d{1,7})(?:-|\s)(\d{1,6})(?:-|\s)([0-9])))$"
        ISBN13_NUMBER = "\d"
        matcher = re.search(ISBN13_REGEX, code)
        if matcher is None:
            return False
        code = ''.join(re.findall(ISBN13_NUMBER, code))
        sum = 0
        for i in range(0, 13):
            sum += (1 if i % 2 == 0 else 3) * int(code[i])
        if sum % 10 == 0:
            return True
        return False

    @staticmethod
    def convertToISBN13(code):
        if ISBNValidator.isValidISBN10(code):
            tempCode = '978' + code[:len(code) - 1].replace('-', '')
            sum = 0
            for i in range(0, 12):
                sum += (1 if i % 2 == 0 else 3) * int(tempCode[i])
            code = '978' + ('' if re.search('-', code) is None else '-') + code[:len(code) - 1] \
                   + str(0 if sum % 10 == 0 else 10 - (sum % 10))
            return code if ISBNValidator.isValidISBN13(code) else False
        elif ISBNValidator.isValidISBN13(code):
            return code
        else:
            return False

    @staticmethod
    def convertToISBN10(code):
        if ISBNValidator.isValidISBN13(code):
            code = code[3:len(code) - 1]
            if code[0] == '-':
                code = code[1:]
            tempCode = code.replace('-', '')
            sum = 0
            for i in range(1, 10):
                sum += i * int(tempCode[9 - i])
            code = code + str('X' if sum % 11 == 10 else sum % 11)
            return code if ISBNValidator.isValidISBN10(code) else False
        elif ISBNValidator.isValidISBN10(code):
            return code
        else:
            return False
