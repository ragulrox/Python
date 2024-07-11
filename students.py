class Student:
    def __init__(self, name, marks_subj1, marks_subj2, marks_subj3):
        self.name = name
        self.marks_subj1 = marks_subj1
        self.marks_subj2 = marks_subj2
        self.marks_subj3 = marks_subj3

    def calculate_total_marks(self):
        return self.marks_subj1 + self.marks_subj2 + self.marks_subj3

# Creating instances for 2 students
student1 = Student("Alice", 85, 92, 78)
student2 = Student("Bob", 76, 88, 90)

# Calculating and printing total marks
print(f"{student1.name}'s total marks: {student1.calculate_total_marks()}")
print(f"{student2.name}'s total marks: {student2.calculate_total_marks()}")
