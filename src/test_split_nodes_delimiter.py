import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_node_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)    
        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)])
    def test_split_node_delimiter_2(self):
        node = TextNode("This is `text with` a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)    
        self.assertEqual(new_nodes,[
            TextNode("This is ", TextType.TEXT),
            TextNode("text with", TextType.CODE),
            TextNode(" a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)])
    def test_split_node_delimiter_3(self):
        node = TextNode("This is text with` a `code block` word", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)    
    def test_split_node_delimiter_4(self):
        node = TextNode("This is *text with* a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)    
        self.assertEqual(new_nodes,[
            TextNode("This is *text with* a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)])   
    def test_split_node_delimiter_5(self):
        node = TextNode("**a** b **c**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)    
        self.assertEqual(new_nodes,[
            TextNode("a", TextType.BOLD),
            TextNode(" b ", TextType.TEXT),
            TextNode("c", TextType.BOLD)])
    def test_split_node_delimiter_6(self):
        node = TextNode("x **a** y **b** z", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)    
        self.assertEqual(new_nodes,[
            TextNode("x ", TextType.TEXT),
            TextNode("a", TextType.BOLD),
            TextNode(" y ", TextType.TEXT),
            TextNode("b", TextType.BOLD),
            TextNode(" z", TextType.TEXT)]),
    def test_split_node_delimiter_7(self):
        node = TextNode("bb**bb**bbb", TextType.TEXT)
        node2 = TextNode("aaaaaa", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node,node2], "**", TextType.BOLD)    
        self.assertEqual(new_nodes,[
            TextNode("bb", TextType.TEXT),
            TextNode("bb", TextType.BOLD),
            TextNode("bbb", TextType.TEXT),
            TextNode("aaaaaa", TextType.BOLD),
        ])
if __name__ == "__main__":
    unittest.main()
