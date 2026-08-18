
import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
#    def test_eq(self):
#        node = TextNode("This is a text node", TextType.BOLD)
#        node2 = TextNode("This is a text node", TextType.BOLD)
#        self.assertEqual(node, node2)
#    def test_not_eq(self):
#        node = TextNode("This is a text node", TextType.BOLD)
#        node2 = TextNode("This is not a text node", TextType.BOLD)
#        self.assertNotEqual(node,node2)
#    def test_not_eq2(self):
#        node = TextNode("This is a text node", TextType.BOLD)
#        node2 = TextNode("This is a text node", TextType.LINK)
#        self.assertNotEqual(node,node2)
#    def test_not_eq3(self):
#        node = TextNode("This is a text node", TextType.BOLD)
#        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.google.com")
#        self.assertNotEqual(node,node2)
#    def test_eq2(self):
#        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
#        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.google.com")
#        self.assertEqual(node,node2)
    def test_voidNode(self):
        node = HTMLNode(None,None,None,None)
        res = node.props_to_html()
        self.assertEqual(res,"")
    def test_voidProps(self):
        node = HTMLNode("p","Lorem Ipsum","https://www.google.com",None)
        res = node.props_to_html()
        self.assertEqual(res,"")
    def test_propsWorking(self):
        node = HTMLNode("p","Lorem Ipsum","https://www.google.com",
        {"href": "https://www.google.com","target": "_blank"})
        res = node.props_to_html()
        expectedRes = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(res,expectedRes)
if __name__ == "__main__":
    unittest.main()
