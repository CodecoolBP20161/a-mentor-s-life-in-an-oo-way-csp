from person import Person
import csv


class Mentor(Person):
    def __init__(self, nickname, *args):
        super().__init__(*args)
        self.nickname = nickname


    def poledance(self, energy_level, happines_level):
        self.energy_level += 4
        self.happines_level += 8

    @classmethod
    def create_by_csv(cls, file_name):
        mentor_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i in reader:
                mentor_list.append(Mentor(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return mentor_list

file_name = "data/mentors.csv"
x = Mentor.create_by_csv(file_name)
