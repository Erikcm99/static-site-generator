from textnode import TextNode
from textnode import TextType
from copy_recursive import copy_recursive
import os
def main():
    path = os.path.dirname(__file__)
    copy_recursive(os.path.join(path,"../static/"),os.path.join(path,"../public/"))
    text_node = TextNode("AAA",TextType.LINK,"aaaa")
    print(text_node)
main()
