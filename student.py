from person import Person
import csv


class Student(Person):
    knowledge_level = 0
    retrospective_object = ''

    def __init__(self, knowledge_level, retro, *args):
        print('Student class init')
        self.knowledge_level = knowledge_level
        self.retrospective_object = retro
        super().__init__(*args)

    @classmethod
    def create_by_csv(cls, file_name):
        return_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                return_list.append(cls(*row))
        return return_list

# Mark = Student()
list1 = Student.create_by_csv("students.csv")
print(list1[0].first_name, list1[0].last_name, list1[0].gender)
