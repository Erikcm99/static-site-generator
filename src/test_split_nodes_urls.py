import unittest
from extract_urls import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
from split_nodes_urls import split_nodes_image, split_nodes_link

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and more text",
        TextType.TEXT,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and more text", TextType.TEXT),
            ],new_nodes)
    def test_split_nodes_link(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
             TextNode("This is text with a link ", TextType.TEXT),
             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
             TextNode(" and ", TextType.TEXT),
             TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
             ], new_nodes)
if __name__ == "__main__":
    unittest.main()
