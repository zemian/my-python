import unittest
import random

class PythonCoreFeatures(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(0.1 + 0.2, 0.3)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, 5)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(' '), ['hello', 'world'])
        self.assertEqual('a '.split(' '), ['a', ''])
        self.assertEqual(' a'.split(' '), ['', 'a'])
        self.assertEqual(' a '.split(' '), ['', 'a', ''])
        self.assertEqual(' '.split(' '), ['', ''])
        self.assertEqual(''.split(' '), [''])
        self.assertEqual('abc'.split(':'), ['abc'])
        self.assertRaises(ValueError, 'abc'.split, '')  # We cannot call split with empty string!
        self.assertEqual(list('abc'), ['a', 'b', 'c'])  # This is how to split a string into letters

        # Alternate way to test exception
        with self.assertRaisesRegex(ValueError, 'empty separator'):
            'abc'.split('')

        self.assertEqual('a:b:c:'.split(':'), ['a', 'b', 'c', ''])
        # Note that last separator is NOT trimmed
        self.assertEqual('Roses are red\nViolets are blue\n'.split("\n"), ['Roses are red', 'Violets are blue', ''])

        # Split by default return list of words, but noted that last separator is trimmed!
        self.assertEqual('Roses are red\nViolets are blue\n'.split(), ['Roses', 'are', 'red', 'Violets', 'are', 'blue'])

    def test_shuffle(self):
        seq = list(range(10))
        random.shuffle(seq)
        seq.sort()
        self.assertEqual(seq, list(range(10)))