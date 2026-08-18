from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type,url=None):
        self.text = text
        self.text_type = text_type
        if url:
            self.url = url
        else:
            self.url = None

    def __eq__(self,other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
 
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK and text_node.url:
        return LeafNode("a", text_node.text,{'href':text_node.url})
    elif text_node.text_type == TextType.IMAGE and text_node.url:
        return LeafNode("img", "",{'src':text_node.url, 'alt':text_node.text})
    raise Exception("No coincide con ningun tipo")
