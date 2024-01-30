from pathlib import Path

def search_file(filename_part, extension, path, recursive=True):
    path = Path(path)
    if recursive:
        files = path.rglob(f"*{filename_part}*{extension}")
    else:
        files = path.glob(f"*{filename_part}*{extension}")
    return list(files)

def search_dir(dirname_part, path, recursive=True):
    path = Path(path)
    if recursive:
        dirs = path.rglob(f"*{dirname_part}*")
    else:
        dirs = path.glob(f"*{dirname_part}*")
    return [dir for dir in dirs if dir.is_dir()]

# example
test_dir = Path("path_to_directory")

# Find all files with .txt extension
txt_files = search_file("", ".txt", test_dir, recursive=True)
print("All .txt files: ", txt_files)

# Find all files with .csv extension
csv_files = search_file("", ".csv", test_dir, recursive=True)
print("All .csv files: ", csv_files)

# Find a directory, which name contains "третья"
dir_containing_text = search_dir("третья", test_dir, recursive=True)
print("Directory containing the text 'третья': ", dir_containing_text)

# Find a file, which starts with "."
hidden_files = search_file(".", "", test_dir, recursive=True)
print("All files starting with '.': ", hidden_files)
