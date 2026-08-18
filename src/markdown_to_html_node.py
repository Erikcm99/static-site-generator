from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnode
from textnode import text_node_to_html_node
from parentnode import ParentNode

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    print(f"\n\n#########BLOCKS:{blocks}##########")
    first_parent = ParentNode("div",[])
    for block in blocks:
        type = block_to_block_type(block)
        if type == BlockType.PARAGRAPH:
            clean_paragraph = clean_paragraph_markdown(block)
            children = text_to_children(clean_paragraph)
            parent = ParentNode("p",children)
            first_parent.children.append(parent)
        elif type == BlockType.CODE:
            children = text_to_children(block)
        elif type == BlockType.HEADING:
            clean_header_tuple = clean_header_markdown(block)
            children = text_to_children(clean_header_tuple[0])
            parent = ParentNode(f"h{clean_header_tuple[1]}",children)

            first_parent.children.append(parent)

        elif type == BlockType.ORDERED_LIST:
            children = text_to_children(block)
        elif type == BlockType.UNORDERED_LIST:
            children = text_to_children(block)
        elif type == BlockType.QUOTE:
            return first_parent 
    return first_parent



def clean_header_markdown(text: str):
    count = text.count("#")
    stripped_text = text.strip("#")
    stripped_text = stripped_text.strip()
    return (stripped_text,count)

def clean_paragraph_markdown(text: str):
    print(f"text:{text}")
    stripped_text = text.strip()
    stripped_text = text.replace("\n"," ")
    stripped_text = text.strip()
    print(f"stripped_text: {stripped_text}")
    return stripped_text

def text_to_children(text):
    children = []
    print(f"\ntext:{text}")
    text_nodes = text_to_textnode(text)
    print(f"text to textNode: {text_nodes}")
    for node in text_nodes:
        print(f"textnode to htmlNode: {text_node_to_html_node(node)}")
        children.append(text_node_to_html_node(node))
    print("\n")
    return children


