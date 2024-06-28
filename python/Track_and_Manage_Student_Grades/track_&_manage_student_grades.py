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

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, letter_grade):
        gpa_scale = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        return gpa_scale.get(letter_grade, 0.0)

    def display_grades(self):
        print("Grades by subject:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

    def display_summary(self):
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(letter_grade)

        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

    def save_grades(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.grades, file)

    def load_grades(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.grades = json.load(file)

def main():
    student_grades = StudentGrades()
    
    while True:
        action = input("Choose an action: [add/display/summary/exit]: ").strip().lower()
        
        if action == 'add':
            subject = input("Enter subject: ").strip()
            grade = float(input("Enter grade: "))
            student_grades.add_grade(subject, grade)
        elif action == 'display':
            student_grades.display_grades()
        elif action == 'summary':
            student_grades.display_summary()
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
