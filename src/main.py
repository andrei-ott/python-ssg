import os
import shutil
from block_markdown import markdown_to_html_node
from pathlib import Path

def clear_directory(dir_path):
    if not os.path.exists(dir_path):
        return
    if not os.path.isdir(dir_path):
        raise NotADirectoryError(f"The path '{dir_path}' is not a directory.")
    
    shutil.rmtree(dir_path)
    os.mkdir(dir_path)


def copy_directory_contents(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"The directory '{src_dir}' does not exist.")
    if not os.path.isdir(src_dir):
        raise NotADirectoryError(f"The path '{src_dir}' is not a directory.")
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"The directory '{dest_dir}' does not exist.")
    if not os.path.isdir(dest_dir):
        raise NotADirectoryError(f"The path '{dest_dir}' is not a directory.")

    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        if os.path.isdir(src_item):
            os.mkdir(dest_item)
            copy_directory_contents(src_item, dest_item)
        else:
            shutil.copy(src_item, dest_item)


def extract_title(markdown):
    if not markdown.startswith("# "):
        raise Exception("Markdown must start with title")
    
    return markdown.split("\n", 1)[0][2:]


def read_file_content(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"The path '{file_path}' is a directory, not a file.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file_content(dest_path, content):
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(content)
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from\n{from_path}\nto\n{dest_path}\nusing\n{template_path}")

    from_path_content = read_file_content(from_path)
    template_path_content = read_file_content(template_path)

    from_path_title = extract_title(from_path_content)
    from_path_html = markdown_to_html_node(from_path_content).to_html()

    template_path_content = template_path_content.replace("{{ Title }}", from_path_title)
    template_path_content = template_path_content.replace("{{ Content }}", from_path_html)

    write_file_content(dest_path, template_path_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        content_item = os.path.join(dir_path_content, item)
        
        if os.path.isdir(content_item):
            generate_pages_recursive(content_item, template_path, os.path.join(dest_dir_path, item))
        else:
            content_path = Path(content_item)
            if content_path.suffix != ".md":
                continue
            
            dest_item = os.path.join(dest_dir_path, content_path.stem + ".html")
            generate_page(content_item, template_path, dest_item)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    public_directory_path = os.path.join(script_dir, "../public")
    static_directory_path = os.path.join(script_dir, "../static")

    clear_directory(public_directory_path)
    copy_directory_contents(static_directory_path, public_directory_path)

    from_path = os.path.abspath(os.path.join(script_dir, "../contents"))
    template_path = os.path.abspath(os.path.join(script_dir, "../template.html"))
    dest_path = os.path.abspath(os.path.join(script_dir, "../public"))

    generate_pages_recursive(from_path, template_path, dest_path)


main()