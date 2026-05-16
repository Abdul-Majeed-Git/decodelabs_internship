======================
  Password generator
======================

Author   | Abdul-Majeed
Language | Python 3.12
Libraries| random , secrets , string 

============
Description:
============
This project is secure CLI-base program that allow users to generate secure random Password in python.
It allows users to generate highly secure, random passwords using cryptographic-grade security.

=========
Features:
=========
->| Quick generation of a 20-character secure password.
->| allows users to generate password of their own choice of length.
->| Password includes mix type of character(uppercase , lowercase, digits , special symbols).
->| Handles sudden exits (ctrl +c on linux) and invalid menu choices.

=======================
How to run the project?
=======================
| Make sure you have python 3 installed on your system.

|Steps to run:
1. Open your terminal or VS code terminal.
2. Navigate to the project directory.
3. Type the following command: | python pwd_generator.py 

============
How to use ?
============
When you run the script the menu will appear.
Type 1: Generate a standard secure 20-character password.
Type 2: Prompt asks for custom length(maximum 64), then enter any number.
Type 3: Type 'Q' or 'q', safely exits the application