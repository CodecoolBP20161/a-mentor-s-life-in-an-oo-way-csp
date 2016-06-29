from mentor import Mentor
from student import Student


class CodecoolClass:
    self.mentors = []
    self.students = []
    self.location = "Budapest"
    self.year = "2016"
    self.events = []
    self.retrospectives = []

    '''def __init__(self, location, year, mentors, students, retrospectives, events):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students
        # self.retrospectives = !!!!!!!!!!!!!!!!!!!!
        self.events = Event.event_list'''

    @classmethod
    def generate_local(cls):
        cls.mentors = Mentor.create_by_cs("/data/mentors.csv")
        cls.students = Student.create_by_csv("/data/students.csv")
        cls.events = Event.create_by_csv("/data/events.csv")
        for student in cls.students:
            cls.retrospectives.append(student.retrospective_object)
            
        # cls.retrospectives =
        # return CodecoolClass
