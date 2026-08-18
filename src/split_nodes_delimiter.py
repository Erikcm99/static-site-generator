from textnode import TextNode, TextType
from typing import List
def split_nodes_delimiter(old_nodes:List[TextNode], delimiter: str, text_type: TextType):
    if not old_nodes or not delimiter or not text_type:
        raise Exception(f"old_nodes:{old_nodes}, delimiter:{delimiter},text_type:{text_type}")
    result = []
    for node in old_nodes:
        elements_without_delimiter = node.text.split(delimiter)
        delimiter_count = node.text.count(delimiter)
        if delimiter_count % 2 != 0:
            raise Exception("A closing delimiter was not found")
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            for i in range(len(elements_without_delimiter)):
                element = elements_without_delimiter[i]
                if len(element) > 0:
                    if i % 2 == 0:
                        result.append(TextNode(element, TextType.TEXT))
                    else:
                        result.append(TextNode(element, text_type))

    return result



