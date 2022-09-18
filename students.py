class Student:
    """assigning a class of student"""
    next_grade = 1
    def __init__(self, name, age, grade):
        """intintialize attributes"""
        self.name = name
        self.age = age
        self.grade = grade
    def details(self):
        return '{} {} {}'.format(self.name, self.age, self.grade)
    def next_class(self):
        self.grade = self.grade + self.next_grade
student_1 = Student('andrew', 11, 6)
print(student_1.details())
print(student_1.grade)
student_1.next_class()
print(student_1.grade)
print(Student.__dict__)