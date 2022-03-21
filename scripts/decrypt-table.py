import string


def translate_letters_demo():
    def shift_letters(letters, step):
        return letters[step:] + letters[0:step]

    # Encoding
    letters = string.ascii_uppercase
    table = str.maketrans(letters, shift_letters(letters, 3))
    code = 'HELLO WORLD!'.translate(table)
    print(code) # KHOOR ZRUOG!

    # Decoding
    code = 'KHOOR ZRUOG!'
    table_reverse = str.maketrans(shift_letters(letters, 3), letters)
    text = code.translate(table_reverse)
    print(text)


def char_ordinal_demo():
    char_int = ord('Z')
    print("'Z' value is " + str(char_int))
    letter = chr(char_int)
    print("Reverse of ordinal value is " + letter)
    print("'A' + 5 is " + chr(ord('A') + 3))

char_ordinal_demo()
