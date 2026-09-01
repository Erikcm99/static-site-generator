from textnode import TextNode
from textnode import TextType
from copy_recursive import copy_recursive
from generate_page import generate_page, generate_page_recursive
import os
def main():
    path = os.path.dirname(__file__)
    copy_recursive(os.path.join(path,"../static/"),os.path.join(path,"../public/"))
    generate_page_recursive(os.path.join(path,"../content"),os.path.join(path,"../template.html") ,os.path.join(path,"../public"))
    #generate_page(os.path.join(path,"../content/index.md"),os.path.join(path,"../template.html") ,os.path.join(path,"../public/index.html"))
main()
