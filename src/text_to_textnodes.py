from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_urls import split_nodes_image, split_nodes_link

def text_to_textnode(text):
    result = []
    node = TextNode(text, TextType.TEXT)
    result = (split_nodes_delimiter([node],'`',TextType.CODE))
    result = (split_nodes_delimiter(result,'**',TextType.BOLD))
    result = (split_nodes_delimiter(result,'_',TextType.ITALIC))
    result = (split_nodes_image(result))
    result = (split_nodes_link(result))
    return result
    
