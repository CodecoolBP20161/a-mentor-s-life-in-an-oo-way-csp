from person import Person
import csv
from retro import Retro


class Student(Person):
    knowledge_level = 0
    retrospective_object = ''

    def __init__(self, knowledge_level, retro, *args):
        self.knowledge_level = knowledge_level
        self.retrospective_object = retro
        super().__init__(*args)

    @classmethod
    def create_by_csv(cls, file_name):
        student_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                retro = Retro(row[1])
                student_list.append(cls(int(row[0]), retro, row[2], row[3], row[4], row[5], int(row[6]), int(row[7])))
        return student_list

    def knowledge_level_changer(self, delta):
        self.knowledge_level += int(delta)
        return self.knowledge_level
