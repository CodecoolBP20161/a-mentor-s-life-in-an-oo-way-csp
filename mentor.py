from person import Person
import csv


class Mentor(Person):
    def __init__(self, nickname, *args):
        super().__init__(*args)
        self.nickname = nickname

    def poledance(self, School):
        print("Dani : 'Vu le vo ku se avekvá, szeszvá'")
        for student in School.students:
            student.energy_level_changer(15)
            student.happiness_level_changer(15)

    @classmethod
    def create_by_csv(cls, file_name):
        mentor_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i in reader:
                mentor_list.append(Mentor(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return mentor_list
