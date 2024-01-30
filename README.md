Bruteforce Password Cracker

This Python script is a simple brute-force password cracker that demonstrates the concept of attempting to crack a password through successive guesses. The script utilizes a system stub to simulate authentication attempts against a set of passwords stored in a file.

Description

The project consists of the following files:

main.py: This file contains the main logic of the password cracker. It imports the bf module to read passwords from a file and attempts to authenticate using a brute-force approach.

bf.py: This module provides a function to read passwords from a file.
Functionality

The SystemStub class simulates a system with a login and a password. It has an auth() method to attempt authentication.

The do_bruteforce() function attempts to crack the password by trying each password from a file using the SystemStub's authentication method.

If a matching password is found, it's printed; otherwise, a message indicating that the password was not found is displayed.
Usage

To run the password cracker:

Navigate to the directory containing the project files.

Run the following command:

$ python3 main.py

Note: Make sure you have navigated to the correct directory where the main.py and bf.py files are located.

Recommendations

It's recommended to navigate to the project directory before running the script to ensure that the file paths are resolved correctly.
