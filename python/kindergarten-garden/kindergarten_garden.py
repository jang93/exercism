STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
            'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

PLANT_MAP = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}

class Garden:
    def __init__(self, diagram='', students=STUDENTS):
        self.diagram = diagram
        self.students = sorted(students, key=lambda x: x[0])
        self.plants_map = self.breakdown()

    def breakdown(self):
        plants_map = {}
        rows_list = self.diagram.split('\n')
        for i in range(len(rows_list[0])//2):
            plants_map[self.students[i]] = [PLANT_MAP[plant] for row in rows_list for plant in row[i*2:i*2+2]]
        return plants_map

    def plants(self, student):
        return self.plants_map[student]
