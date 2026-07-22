# Student-Gradebook-Manager

Final Python Project - Student Gradebook Manager



\## Full Name

Hosna Hussaini



\##Project Title

Student Gradebook Manager



\## Project Description

This project is a Student Gradebook Manager developed using Python and Object-Oriented-Programming (OOP). It allows users to add and manage students, courses, assessments, and grades.

The system can also calculate averages. generate student reports, assign letter grades, and display teacher comments.



\## How to Run the Project

1. Open the project in PyCharm or another Python IDE.
2. Run the 'main.py' file.
3. Use the menu to add students, courses, assessments, record grades, and generate reports.



\## Classes Created

* Student
* Course
* Assessment
* Quiz
* Exam
* Project
* Gradebook



\## Encapsulation

Encapsulation is used in the 'Student' class. The email attribute is private and can only be accessed or modified using getter and setter methods. 



\## Inheritance 

The 'Quiz', 'Exam', and 'Project' classes inherit from the 'Assessment' class. They reuse the common attributes and methods from the parent class.



\## Method Overriding 

The 'display\_info()' method is overridden in the 'Quiz', 'Exam', and 'Project' classes to display information specific to each assessment type.



\## Custom Features

1. Letter Grade generation based on the student's average score.
2. Teacher Comment based on the student's performance.



