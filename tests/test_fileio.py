import unittest

class FileIO(unittest.TestCase):
    def test_open_read(self):
        with open('test_fileio.py', 'r') as f:
            lines = f.read().split("\n")
            self.assertGreaterEqual(len(lines), 9)

    def test_open_readlines(self):
        with open('test_fileio.py', 'r') as f:
            lines = f.readlines()  # It will trim last new line!
            self.assertGreaterEqual(len(lines), 12)

    def test_open_for_loop(self):
        with open('test_fileio.py', 'r') as f:
            count = 0
            # Note that it does loop through the new line (empty text) last
            for _ in f:
                count += 1
            self.assertGreaterEqual(count, 20)
