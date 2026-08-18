from typing import List
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children: List,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Element without tag")
        if not self.children:
            raise ValueError("Parent without children")

        result = f"<{self.tag}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result

