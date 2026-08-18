def markdown_to_blocks(markdown: str):
    markdown = markdown.strip()
    splitted = markdown.split("\n\n")
    if len(splitted) > 0:
        x = lambda a : len(a) > 0
        splitted = list(filter(x, splitted))
    return splitted

