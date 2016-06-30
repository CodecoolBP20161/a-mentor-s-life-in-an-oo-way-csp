import csv
import random


class Education():
    def __init__(self, name, delta_knowledge_level, delta_happiness_level):
        self.name = name
        self.delta_knowledge_level = delta_knowledge_level
        self.delta_happiness_level = delta_happiness_level

    @classmethod
    def create_by_csv(cls, file_name):
        education_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for education in reader:
                education_list.append(Education(education[0], education[1], education[2]))
        return education_list

    @staticmethod
    def peer_mentoring(School):
        student_1 = random.choice(School.students)
        student_2 = random.choice(School.students)
        while student_1 == student_2:
            student_2 = random.choice(School.students)
        print("\n" + "The participants are :")
        print(student_1.first_name, student_1.last_name, student_2.first_name, student_2.last_name)
        print("Knowledge and happiness level before the mentoring:")
        print(student_1.knowledge_level, student_1.happiness_level, student_2.knowledge_level, student_2.happiness_level)
        for i in School.students:
            if i == student_1:
                i.knowledge_level_changer(School.educations[2].delta_knowledge_level)
                i.happiness_level_changer(School.educations[2].delta_happiness_level)
            elif i == student_2:
                i.knowledge_level_changer(School.educations[2].delta_knowledge_level)
                i.happiness_level_changer(School.educations[2].delta_happiness_level)

        # pressenter = input()
        print("Knowledge and happiness level after the mentoring:")
        print(student_1.knowledge_level, student_1.happiness_level, student_2.knowledge_level, student_2.happiness_level)

    @staticmethod
    def private_mentoring(School):
        student = random.choice(School.students)
        mentor = random.choice(School.mentors)

        print("\n" + "The participants are :")
        print(student.first_name, student.last_name, mentor.first_name, mentor.last_name)
        print("Knowledge and happiness level before the mentoring:")
        print(student.knowledge_level, student.happiness_level)
        for i in School.students:
            if i == student:
                i.knowledge_level_changer(School.educations[3].delta_knowledge_level)
                i.happiness_level_changer(School.educations[3].delta_happiness_level)
        for i in School.mentors:
            if i == mentor:
                i.happiness_level_changer(School.educations[3].delta_happiness_level)

        # pressenter = input()
        print("Knowledge and happiness level after the mentoring:")
        print(student.knowledge_level, student.happiness_level)
        print("The happiness of the mentor increased by " + School.educations[3].delta_happiness_level)

    @staticmethod
    def not_exam(School):
        student = random.choice(School.students)
        mentor = random.choice(School.mentors)
        print("\n" + "The participants are :")
        print(student.first_name, student.last_name, mentor.first_name, mentor.last_name)
        print("Knowledge and happiness level before the exam:")
        print(student.knowledge_level, student.happiness_level)
        result = random.randint(0, 49)
        # press = input()
        if result < 50:
            print("Sorry my friend, this was not enough, you are fired and have to pay all of the tuition fee.")
            for i in School.students:
                if i == student:
                    i.knowledge_level = -1000
                    i.happiness_level = -1000
            print("Knowledge and happiness level after the exam:")
            print(student.knowledge_level, student.happiness_level)
            # press = input()
            print("You sucked it, potato head, it was just a joke.")
