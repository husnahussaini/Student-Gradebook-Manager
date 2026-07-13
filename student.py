class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.__email = email
        self.courses = []

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def set_email(self, email):
        if "@" and "." in email:
            self.__email = email
            return True
        else:
            print("Invalid email address!")
            return False

    def get_email(self):
        return self.__email

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
        else:
            print("Student is already enrolled in this course!")

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")
        if self.courses:
            print("Courses:", ", ".join(self.courses))
        else:
            print("Courses: None")
