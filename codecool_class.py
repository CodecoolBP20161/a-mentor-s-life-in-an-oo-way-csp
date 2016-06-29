from mentor import Mentor
from student import Student
from event import Events
from retro import Retro
from education import Education


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
