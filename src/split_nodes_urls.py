from extract_urls import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        old_section = ""
        alt_text = ""
        url = ""

        if len(matches) == 0:
            new_nodes.append(node)
        else:
            for match in matches:
                alt_text = match[0]
                url = match[1]
                if len(old_section) > 0:
                    section = old_section.split(f"![{alt_text}]({url})",1)
                else:
                    section = node.text.split(f"![{alt_text}]({url})",1)
                old_section = section[1]
                if len(section[0]) > 0:
                    new_node = TextNode(section[0],TextType.TEXT)
                    new_nodes.append(new_node)
                new_node = TextNode(alt_text,TextType.IMAGE,url)
                new_nodes.append(new_node)
            if len(old_section) > 0:
                new_node = TextNode(old_section,TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes
                # si seccion [0] es string vacio significa que la imagen no tiene texto detras
                # sino primero se crea el texto 
def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        old_section = ""
        alt_text = ""
        url = ""

        if len(matches) == 0:
            new_nodes.append(node)
        else:
            for match in matches:
                alt_text = match[0]
                url = match[1]
                if len(old_section) > 0:
                    section = old_section.split(f"[{alt_text}]({url})",1)
                else:
                    section = node.text.split(f"[{alt_text}]({url})",1)
                old_section = section[1]
                if len(section[0]) > 0:
                    new_node = TextNode(section[0],TextType.TEXT)
                    new_nodes.append(new_node)
                new_node = TextNode(alt_text,TextType.LINK,url)
                new_nodes.append(new_node)
            if len(old_section) > 0:
                new_node = TextNode(old_section,TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes
                # si seccion [0] es string vacio significa que la imagen no tiene texto detras
                # sino primero se crea el texto 
