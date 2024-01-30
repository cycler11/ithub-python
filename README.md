File and Directory Search Utility

This utility script allows users to search for files and directories within a specified path. It provides flexibility in searching by filename parts, extensions, and directory names.

Function Parameters

filename_part: A part of the filename to search for.
extension: The file extension to filter by.
path: The directory path to search within.
recursive: If True, search recursively within subdirectories; otherwise, search only within the specified directory.

Example Use Cases

1. Finding Specific File Types: You can search for specific file types by specifying the filename part and extension.

2. Locating Directories: Easily locate directories containing specific terms or patterns in their names.

3. Recursive or Non-Recursive Search: Choose whether to search recursively within subdirectories or limit the search to the specified directory.

Notes

Ensure that the Python script using this utility has appropriate read permissions for the directories being searched.
This script utilizes Python's pathlib module, which provides an object-oriented interface for filesystem paths.
