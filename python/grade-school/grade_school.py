class School:
    def __init__(self):
        self.database = {}

    def add_student(self, name, grade):
        self.database[grade] = sorted(self.database.get(grade, []) + [name])

    def roster(self):
        return [student for grade in sorted(self.database.keys()) for student in self.database[grade]]

    def grade(self, grade_number):
        return self.database.get(grade_number, [])
