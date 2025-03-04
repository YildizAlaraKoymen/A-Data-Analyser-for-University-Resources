# A-Data-Analyser-for-University-Resources
An application for analysing the allocation of university resources across different departments using object oriented principles.

Overview
This project is a Python-based application designed to analyze university resource allocation across different departments. The application processes department and course data from input text files and provides various insights such as department sizes, instructor courses, and course popularity trends.

Python Version
This project was developed using Python 3.11.

Operating System
This project was developed and tested on Windows 11.

Functionalities
Load University Data: Reads department and course details from input files.
Print Lab Courses: Displays all courses with lab sections and their total capacities.
Print Department Sizes: Generates a pie chart displaying department-wise student distribution.
Print Instructor Courses: Prompts the user for an instructor’s name and lists their courses.
Print Unpopulated Courses: Identifies courses with fewer than 5 registered students.
Print Multi-Section Courses: Lists courses with multiple sections.
Print Top Courses: Shows the most enrolled courses per department.

Class Structure
University Class
Stores university details and department objects.
Loads data from input files and processes courses.
Implements analysis and reporting functions.

Department Class
Stores department attributes and associated courses.
Provides helper functions for analyzing department data.

Course Class
Stores general course details and sections.
Supports operations such as computing total capacity and registrations.

LabCourse Class (Subclass of Course)
Stores additional lab-specific details.
Supports tracking of lab sections and capacities.

Possible Improvements
Enhance Data Visualization: Improve charts using advanced visualization libraries like Seaborn.
GUI Integration: Develop a user-friendly graphical interface for easier interaction.
Database Integration: Store and retrieve course data using a database instead of text files.
Automated Testing: Implement unit and integration tests using pytest for reliability.
Performance Optimization: Optimize file parsing and data processing for large datasets.
Web-based Dashboard: Extend the application into a web-based dashboard for real-time analysis.
