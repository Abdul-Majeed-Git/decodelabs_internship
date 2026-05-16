=======================
    To-Do List App      
=======================

Author   | Abdul-Majeed
Language | Python 3.12
Libraries| json

============
Description:
============
This project is a lightweight, CLI-based To-Do List application written in Python. 
It helps users manage their daily tasks efficiently from the terminal while keeping the data persistent.

=========
Features:
=========
->| Persistent storage using a local JSON file (list.json) so data is never lost.
->| Quick and easy creation of tasks with auto-incremented tracking IDs.
->| Clean sequence view of all existing tasks in the list.
->| Secure deletion mechanism that handles empty states and dynamically re-indexes task IDs.
->| Auto-loads previous tasks immediately upon starting the application.

=======================
How to run the project?
=======================
| Make sure you have Python 3 installed on your system.

| Steps to run:
1. Open your terminal or VS Code terminal.
2. Navigate to the project directory.
3. Type the following command: | python todo_app.py 

============
How to use?
============
When you run the script, the menu will appear:
Type 1: Prompts you to enter a new task and adds it to the list.
Type 2: Displays all your saved tasks with their respective numbers.
Type 3: Shows the list and asks for the specific number you want to delete.
Type 4: Safely exits the application.