from copy_recursive import copy_recursive
from generate_page import generate_page_recursive
import os
import sys
def main():
    path = os.path.dirname(__file__)
    if not sys.argv[0]:
        basepath = '/'
    else:
        basepath = sys.argv[0]
    copy_recursive(os.path.join(path,"../static/"),os.path.join(path,"../docs/"))
    generate_page_recursive(os.path.join(path,"../content"),os.path.join(path,"../template.html") ,os.path.join(path,"../docs"), basepath)
    #generate_page(os.path.join(path,"../content/index.md"),os.path.join(path,"../template.html") ,os.path.join(path,"../public/index.html"))
main()
