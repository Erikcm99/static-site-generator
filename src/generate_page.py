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
    with open(template_path,'r') as f:
        template_file = f.read()
    final_html = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)
    
    final_template = template_file.replace("{{ Title }}", title)
    final_template = final_template.replace("{{ Content }}", final_html)
    path = os.path.dirname(__file__)
    final_dest_path = os.path.join(path, dest_path)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    f = open(dest_path, "w")
    f.write(final_template)
    f.close()

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception(f"dir_path_content no existe {dir_path_content} not found")

    for element in os.listdir(dir_path_content):
        element_path = os.path.join(dir_path_content, element)
        print(f"element = {element_path}, is file = {os.path.isfile(element_path)}, is_dir = {os.path.isdir(element_path)}")
        element_path = os.path.join(dir_path_content, element)
        if os.path.isfile(element_path):
            if not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path, exist_ok=True)
            origin = element_path
            dest = os.path.join(dest_dir_path, os.path.basename(element))
            dest_html = dest.replace(".md",".html")
            generate_page(origin,template_path,dest_html)

            print(f"Origin: {origin}")
            print(f"Dest: {dest}")


        if os.path.isdir(element_path):

            element_dest_dir = os.path.join(dest_dir_path,element)
            generate_page_recursive(element_path,template_path,element_dest_dir)

          

