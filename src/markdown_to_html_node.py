from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnode
from textnode import text_node_to_html_node, TextNode, TextType
from parentnode import ParentNode

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    first_parent = ParentNode("div",[])
    for block in blocks:
        type = block_to_block_type(block)
        if type == BlockType.PARAGRAPH:
            clean_paragraph = clean_paragraph_markdown(block)
            children = text_to_children(clean_paragraph)
            parent = ParentNode("p",children)
            first_parent.children.append(parent)
        elif type == BlockType.CODE:
            clean_code = clean_code_markdown(block)
            text_node = TextNode(clean_code, TextType.CODE)
            html_node = text_node_to_html_node(text_node)
            parent = ParentNode("pre",[html_node])
            first_parent.children.append(parent)
        elif type == BlockType.HEADING:
            clean_header_tuple = clean_header_markdown(block)
            children = text_to_children(clean_header_tuple[0])
            parent = ParentNode(f"h{clean_header_tuple[1]}",children)

            first_parent.children.append(parent)

        elif type == BlockType.ORDERED_LIST:
            clean_quote = clean_olist_markdown(block)
            children = text_to_children(clean_quote)
            parent = ParentNode("ol",children)
            first_parent.children.append(parent)

        elif type == BlockType.UNORDERED_LIST:
            clean_quote = clean_ulist_markdown(block)
            children = text_to_children(clean_quote)
            parent = ParentNode("ul",children)
            first_parent.children.append(parent)

        elif type == BlockType.QUOTE:
            clean_quote = clean_quote_markdown(block)
            children = text_to_children(clean_quote)
            parent = ParentNode("blockquote",children)
            first_parent.children.append(parent)

            return first_parent 
    return first_parent



def clean_header_markdown(text: str):
    count = text.count("#")
    stripped_text = text.strip("#")
    stripped_text = stripped_text.strip()
    return (stripped_text,count)

def clean_ulist_markdown(text: str):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(f"<li>{line.strip()[1:].strip()}</li>")

    result = "".join(new_lines)
    return result

def clean_olist_markdown(text: str):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(f"<li>{line.strip()[2:].strip()}</li>")

    result = "".join(new_lines)
    return result

def clean_quote_markdown(text: str):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.strip()[1:].strip())

    result = " ".join(new_lines)
    return result


def clean_code_markdown(text: str):
    stripped_text = text.strip("`")
    lines = stripped_text.split("\n")
    lines = [line.strip() for line in lines if len(line.strip()) > 0]
    result = "\n".join(lines)
    return result + "\n"

def clean_paragraph_markdown(text: str):
    lines = text.split("\n")
    lines = [line.strip() for line in lines]
    result = " ".join(lines)
    return result


def text_to_children(text):
    children = []
    text_nodes = text_to_textnode(text)
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children


