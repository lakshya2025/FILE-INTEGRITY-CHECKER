# FILE-INTEGRITY-CHECKER
* COMPANY*: CODTEC IT SOLUTIONS
* NAME* : RAJESH KUMAR
* INTERN ID* :CT04DL1054
* DOMAIN* : Cyber Security & Ethical Hacking
* DURATION* : 4 WEEKS
* MENTOR* : NEELA SANTOSH
* DESCRIPTION* :Project Description: Python-Based File Integrity Checker
This project involves the development of a command-line tool, implemented in Python, to monitor and verify the integrity of files. The tool leverages cryptographic hash functions to generate unique fingerprints of specified files. By comparing these hash values over time, the tool can detect any unauthorized modifications or corruption that may have occurred. Developed using Visual Studio Code (VS Code), this project aims to provide a simple yet effective solution for ensuring data integrity.

Key Features:

File Hashing: The core functionality involves calculating cryptographic hash values (such as SHA-256 or MD5) for user-specified files. The use of the hashlib library in Python ensures robust and widely accepted hashing algorithms are employed.
Baseline Generation: The tool allows users to generate and store an initial set of hash values for a collection of files, establishing a baseline for integrity checks. This baseline can be saved in a structured format (e.g., a text file or a JSON file).
Integrity Verification: The tool can compare the current hash values of the monitored files against the stored baseline. Any discrepancies indicate that the file has been modified since the baseline was established.
Reporting: Upon verification, the tool provides clear and informative output, indicating whether each monitored file's integrity is intact or if modifications have been detected. This could include the filename and the status (e.g., "Integrity OK," "Modification Detected").
User-Friendly Interface: Designed as a command-line tool, the project aims for a simple and intuitive user interface, allowing users to easily specify files for monitoring, generate baselines, and perform integrity checks.
VS Code Development Environment: The project is being developed within Visual Studio Code, taking advantage of its powerful features such as:
Code Editing: Syntax highlighting, intelligent code completion (IntelliSense), and code formatting enhance the development process.
Integrated Terminal: The built-in terminal allows for seamless execution of the Python script and interaction with the file system.
Debugging Capabilities: VS Code's debugger can be utilized for identifying and resolving any issues within the Python code.
Version Control Integration (Git): VS Code's Git integration facilitates tracking changes, collaborating (if applicable), and managing different versions of the project.
Technical Implementation (Anticipated):

Programming Language: Python
Core Library: hashlib (for cryptographic hashing)
Potential Additional Libraries:
os (for file system operations)
json or configparser (for storing and reading baseline hash data)
argparse (for handling command-line arguments)
Development Environment: Visual Studio Code (VS Code)
Intended Use Cases:

Monitoring critical system files for unauthorized changes.
Verifying the integrity of downloaded files.
Detecting accidental corruption of important data.
Ensuring the consistency of configuration files.
Learning Outcomes:

Through this project, you will gain practical experience in:

Working with file system operations in Python.
Implementing cryptographic hashing using the hashlib library.
Designing and implementing command-line interfaces.
Storing and retrieving data from files.
Utilizing the features and benefits of the Visual Studio Code development environment.
Understanding the fundamental concepts of data integrity and security.
This File Integrity Checker project, developed in VS Code, provides a valuable hands-on experience in building a practical security-focused tool using Python. It emphasizes the importance of data integrity and introduces fundamental techniques for its verification. Good luck with your development! Let me know if you have any specific aspects you'd like to elaborate on or any challenges you encounter along the way.

**OUTPUT**
![Image](https://github.com/user-attachments/assets/c90ab2bd-bd8f-4dbf-abab-22f47f46fa9b)
