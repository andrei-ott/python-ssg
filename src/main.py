import os
import shutil

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


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    public_directory_path = os.path.join(script_dir, "../public")
    static_directory_path = os.path.join(script_dir, "../static")

    clear_directory(public_directory_path)
    copy_directory_contents(static_directory_path, public_directory_path)


main()