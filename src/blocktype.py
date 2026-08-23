from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    heading_regex = r'^(#{1,6} .*)'
    code_regex = r'```\n.*```'
    quote_regex = r'> ?.*'
    unordered_regex = r'- .*'
    ordered_regex = r'\d\. .*'

   
    if re.match(heading_regex, markdown) and "\n"not in markdown:
        return BlockType.HEADING
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    if markdown.startswith(">"):
        for line in markdown.split("\n"):
            if not line.strip().startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if markdown.startswith("- "):
        for line in markdown.split("\n"):
            if not line.strip().startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if markdown.startswith("1. "):
        count = 1
        for line in markdown.split("\n"):
            if not line.strip().startswith(f"{count}. "):
                return BlockType.PARAGRAPH
            count += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

