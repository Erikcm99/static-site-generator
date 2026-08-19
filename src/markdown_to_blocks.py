def markdown_to_blocks(markdown: str):
    markdown = markdown.strip()
    splitted = markdown.split("\n\n")
    if len(splitted) > 0:
        splitted = [item.strip() for item in splitted if len(item.strip()) > 0]
    return splitted

