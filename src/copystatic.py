import os
import shutil

from block_markdown import markdown_to_html_node
from inline_markdown import extract_markdown_title

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    from_contents = from_file.read()
    from_file.close()

    temp_file = open(template_path)
    temp_contents = temp_file.read()
    temp_file.close()

    from_html_node = markdown_to_html_node(from_contents)
    from_html = from_html_node.to_html()
    from_title = extract_markdown_title(from_contents)

    new_temp_contents = temp_contents.replace("{{ Title }}", from_title)
    final_temp_contents = new_temp_contents.replace("{{ Content }}", from_html)

    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    dest_file = open(dest_path, "w")
    dest_file.write(final_temp_contents)
    dest_file.close()