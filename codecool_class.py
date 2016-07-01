from mentor import Mentor
from student import Student
from event import Events
from retro import Retro
from education import Education
import random


class CodecoolClass:

    def __init__(self, location, year, mentors, students, retrospectives, events, educations):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students
        self.retrospectives = retrospectives
        self.events = events
        self.educations = educations

    @classmethod
    def generate_local(cls):
        mentors = Mentor.create_by_csv("data/mentors.csv")
        students = Student.create_by_csv("data/students.csv")
        events = Events.create_by_csv("data/events.csv")
        retrospectives = []
        for student in students:
            retrospectives.append(student.retrospective_object)
        education = Education.create_by_csv("data/education.csv")
        local_codecool_class = cls("Budapest", 2016, mentors, students, retrospectives, events, education)
        return local_codecool_class

    def find_student_by_full_name(self, name):
        for i in self.students:
            temp_name = i.first_name + " " + i.last_name
            if temp_name == name:
                return i
        return "We don't find her\him"

    def find_mentor_by_full_name(self, name):
        for i in self.mentors:
            temp_name = i.first_name + " " + i.last_name
            if temp_name == name:
                return i
        return "We don't find her\him"

    def count_students(self):
        print("\n" + "The number of students", len(self.students))   # print out the students
        print("-"*20 + "\n")
        for student in self.students:
            print(student.first_name + " " + student.last_name)
        print("\n")

    def count_mentors(self):
        print("\n" + "The number of mentors", len(self.mentors))  # print out the mentors
        print("-"*20 + "\n")
        for mentor in self.mentors:
            print(mentor.first_name + " " + mentor.last_name)
        print("\n")

    def check_energy(self):
        energy_level_counter = 0
        for i in self.students:       # We check the enery level of the students
            energy_level_counter += int(i.energy_level)
        energy_level_counter = energy_level_counter//len(self.students)
        print("-"*20)
        print("\n" + "The average energy level of the class is: " + str(energy_level_counter))
        print("\n")
        return energy_level_counter

    def class_do_gym(self, energy_level_counter):
        if energy_level_counter < 70:
            print(self.mentors[1].first_name+" "+self.mentors[1].last_name, ':"Class energy is low guys, lets do some exercises!"' + "\n")
            pressenter = input()
            for i in self.students:
                print(i.gym())
            print("\n")

    def do_project(self):
        print("\n" + "Today we are going to make a " + self.educations[0].name + "\n")
        for student in self.students:
            print("Knowledge and happiness level, before and after:")
            print(student.first_name+" "+student.last_name+" "+str(student.knowledge_level)+
            " "+str(student.happiness_level))
            student.knowledge_level_changer(self.educations[0].delta_knowledge_level)
            student.happiness_level_changer(self.educations[0].delta_happiness_level)
            print(student.first_name+" "+student.last_name+" "+str(student.knowledge_level)+
            " "+str(student.happiness_level))
            print("-"*30)
            pressenter = input()

    def all_class_do_event(self, integer):
        print("\n" + "The event now is:")
        print(self.events[integer].name)
        print("\n" + "The energy and happiness is increased by:", self.events[integer].delta_energy_level,
            self.events[integer].delta_happiness_level)
        for student in self.students:
            student.energy_level_changer(self.events[integer].delta_energy_level)
            student.happiness_level_changer(self.events[integer].delta_happiness_level)
        for mentor in self.mentors:
            mentor.energy_level_changer(self.events[integer].delta_energy_level)
            mentor.happiness_level_changer(self.events[integer].delta_happiness_level)

    def do_retro(self):
        print("\n" + "The retrospectives are the following:")
        counter = 1
        for i in self.retrospectives:
            print(str(counter) + " " + i.description)
            counter += 1

    def do_event_after_school(self):
        for i in self.students:
            rand_num = random.randint(3, 7)
            print(i.first_name, i.last_name + " will do: " + self.events[rand_num].name)
            i.happiness_level_changer(self.events[rand_num].delta_happiness_level)
            i.energy_level_changer(self.events[rand_num].delta_energy_level)
        print("-"*20)
        pressenter = input()
        for i in self.mentors:
            print(i.first_name, i.last_name + " will smoke " + self.events[7].name)
            i.happiness_level_changer(self.events[rand_num].delta_happiness_level)
            i.energy_level_changer(self.events[rand_num].delta_energy_level)
