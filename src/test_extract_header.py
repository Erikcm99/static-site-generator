import unittest
from extract_header import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_header(self):
        markdown = '''# Header funciona'''
        valid = "Header funciona"
        self.assertEqual(valid, extract_title(markdown))

    def test_header2(self):
        markdown = '''HEader no funciona'''
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_header3(self):
        markdown = '''## Header no funciona'''
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
