from gradebook import Gradebook
from student import Student
from course import Course
from assessment import Quiz, Exam, Project

gradebook = Gradebook()

while True:
    print("\n===== Student Gradebook Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Add Assessment")
    print("6. Record Grade")
    print("7. View Student Report")
    print("8. Search Student")
    print("9. Update Student")
    print("10. Delete Student")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)

        print("Student added successfully!")
    elif choice == "2":
        gradebook.view_students()
    elif choice == "3":
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")
        course = Course(course_code, course_name)
        gradebook.add_course(course)
        print("Course added successfully!")
    elif choice == "4":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        gradebook.enroll_student(student_id, course_code)
        print("Student enrolled successfully!")
    elif choice == "5":
        course_code = input("Course Code: ")
        assessment_type = input("Assessment Type (Quiz/Exam/Project): ")
        title = input("Title: ")
        max_score = float(input("Max Score: "))

        if assessment_type.lower() == "quiz":
            assessment = Quiz(title, max_score)
        elif assessment_type.lower() == "exam":
            assessment = Exam(title, max_score)
        elif assessment_type.lower() == "project":
            assessment = Project(title, max_score)
        else:
            print("Invalid assessment type!")
            continue
        gradebook.add_assessment(course_code, assessment)
        print("Assessment added successfully!")
    elif choice == "6":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        assessment_title = input("Assessment Title: ")
        score = float(input("Score: "))
        gradebook.record_grade(student_id, course_code, assessment_title, score)
        print("Assessment record added successfully!")
    elif choice == "7":
        student_id = input("Student ID: ")
        gradebook.show_report(student_id)
    elif choice == "8":
        keyword = input("Enter Student ID or Name: ")
        student = gradebook.search_student(keyword)
        if student:
            student.display_info()
        else:
            print("Student not found!")
    elif choice == "9":
        student_id = input("Student ID: ")
        new_name = input("New Name: ")
        new_email = input("New Email: ")
        gradebook.update_student(student_id, new_name, new_email)
        print("Student updated successfully!")
    elif choice == "10":
        student_id = input("Student ID: ")
        gradebook.delete_student(student_id)
        print("Student deleted successfully!")
    else:
        print("Invalid choice, Please try again.")

