import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "This is an image",{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<img href="https://www.google.com">This is an image</img>')
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!",{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
if __name__ == "__main__":
    unittest.main()
