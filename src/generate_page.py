import os
from markdown_to_html_node import markdown_to_html_node
from extract_header import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(from_path):
        raise Exception(f"from_path no existe {from_path} not found")
    if not os.path.isfile(from_path):
            return f'Error: File not found or is not a regular file: "{from_path}"'
    if not os.path.exists(template_path):
        raise Exception(f"template_path no existe {template_path} not found")
    if not os.path.isfile(template_path):
            return f'Error: File not found or is not a regular file: "{template_path}"'
    with open(from_path,'r') as f:
        from_file = f.read()
        print(from_file)
        f.close()
    with open(template_path,'r') as f:
        template_file = f.read()
        print(template_file)
        f.close()
    final_html = markdown_to_html_node(from_file).to_html()
    title = extract_title(final_html)
    template_file.replace("{{ Title }}", title)

