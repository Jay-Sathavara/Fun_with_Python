import json
import os

class StudentGrades:
    def __init__(self, file_path='grades.json'):
        self.grades = {}
        self.file_path = file_path
        self.load_grades()

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]
        self.save_grades()

    def calculate_average(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_subjects = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_subjects if total_subjects > 0 else 0

    