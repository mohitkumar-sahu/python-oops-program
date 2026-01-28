# Hierarchical Inheritance Example - School System

# Parent class
class School:
    def school_info(self):
        print("Welcome to Sunrise Public School.")
        print("We have students, teachers, and staff.\n")

# Child class 1
class Student(School):
    def role_info(self):
        print("I am a student.")
        print("I attend classes and study.\n")

# Child class 2
class Teacher(School):
    def role_info(self):
        print("I am a teacher.")
        print("I teach students and conduct exams.\n")

# Child class 3
class Staff(School):
    def role_info(self):
        print("I am a staff member.")
        print("I help in managing school operations.\n")

# Creating objects of each subclass
student = Student()
teacher = Teacher()
staff = Staff()

# Calling methods
student.school_info()
student.role_info()

teacher.school_info()
teacher.role_info()

staff.school_info()
staff.role_info()
