import student
from student import Student
from course import Course
from assessment import Assessment, Quiz, Exam, Project

class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self, student):
        self.students[student.get_id()] = student

    def add_course(self, course):
        self.courses[course.course_code] = course

    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]

            student.enroll_course(course_code)
            course.add_student(student_id)


    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            course = self.courses[course_code]
            course.add_assessment(assessment)

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            return
        if course_code not in self.courses:
            return
        course = self.courses[course_code]
        assessment = course.find_assessment(assessment_title)
        if assessment is None:
            return
        if score < 0 or score > assessment.max_score:
            return
        if student_id not in self.grades:
            self.grades[student_id] = {}
        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}
        self.grades[student_id][course_code][assessment_title] = score


    def calculate_average(self, student_id, course_code):
        if student_id not in self.grades:
            return 0
        if course_code not in self.grades[student_id]:
            return 0

        course = self.courses[course_code]
        total = 0
        count = 0

        for assessment in course.assessments:
            if assessment.title in self.grades[student_id][course_code]:
                score = self.grades[student_id][course_code][assessment.title]
                total += assessment.calculate_percentage(score)
                count += 1

        if count == 0:
            return 0
        return total / count

    def get_result(self, average):
        if average >= self.passing_grade:
            return "Passed"
        return "Failed"

    def show_report(self, student_id):
        if student_id not in self.students:
            return

        student = self.students[student_id]

        print("\n===== Student Report =====")
        print(f"Student ID: {student.get_id()}")
        print(f"Name: {student.get_name()}")
        print(f"Email: {student.get_email()}")

        for course_code in student.courses:
            course = self.courses[course_code]

            print(f"\nCourse: {course.course_name}")

            if student_id in self.grades and course_code in self.grades[student_id]:
                for assessment in course.assessments:
                    if assessment.title in self.grades[student_id][course_code]:
                        score = self.grades[student_id][course_code][assessment.title]
                        percentage = assessment.calculate_percentage(score)

                        print(f"{assessment.title}: {score}/{assessment.max_score} = {percentage:.1f}%")

                average = self.calculate_average(student_id, course_code)

                print(f"Average: {average:.2f}")
                print(f"Result: {self.get_result(average)}")

    def search_student(self, keyword):
        keyword = keyword.lower()
        for student in self.students.values():
            if keyword == student.get_id().lower() or keyword in student.get_name().lower():
                return student
        return None

    def delete_student(self, student_id):
        if student_id not in self.students:
            return
        student = self.students[student_id]
        for course_code in student.courses:
            course = self.courses[course_code]

            if student_id in course.students:
                course.students.remove(student_id)
        if student_id in self.grades:
            del self.grades[student_id]
        del self.students[student_id]

