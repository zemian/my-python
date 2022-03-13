from unittest import TestCase


class HelloTest(TestCase):
    def test_print(self):
        print("Testing print statement")
        # We can change the line ending char.
        print("Print with changing end params", end='')
        print("Print after changing end args.")
