from codecool_class import CodecoolClass
from education import Education
from foosballmatch import FoosballMatch
import random

School = CodecoolClass.generate_local()
print("Welcome to Codecool ", School.location + " " + str(School.year))  # print out the welcome text
user_input = input("School.count_students()")
School.count_students()
user_input = input("School.count_mentors()")
School.count_mentors()
user_input = input("energy_level = School.check_energy()")
energy_level = School.check_energy()
user_input = input("School.class_do_gym(energy_level)")
School.class_do_gym(energy_level)
user_input = input("energy_level = School.check_energy()")
energy_level = School.check_energy()
user_input = input()
print(
    "\n" + School.mentors[0].first_name + " " + School.mentors[0].last_name +
    ': "I think that the energy level is optimal."')
user_input = input("School.do_project()")
School.do_project()
user_input = input()
print("Continue the day with NOT EXAM.")
user_input = input("Education.not_exam(School)")
Education.not_exam(School)
user_input = input("School.all_class_do_event(2)")
School.all_class_do_event(2)  # lunch
user_input = input("Education.peer_mentoring(School)")
Education.peer_mentoring(School)
user_input = input("Education.private_mentoring(School)")
Education.private_mentoring(School)
user_input = input("School.mentors[0].poledance(School)")
print(
    School.mentors[0].first_name + " " + School.mentors[0].last_name +
    ' "The boogie is in my legs! Lets do poledance."' + "\n")
School.mentors[0].poledance(School)
user_input = input()
print("Energy level increased by 15")
user_input = input("School.check_energy()")
energy_level = School.check_energy()
user_input = input("School.do_retro()")
School.do_retro()
print("\n" + School.mentors[2].first_name + ': "Thanks guys for the retrospectives."' + "\n")
user_input = input("FoosballMatch()")
match = FoosballMatch()
winner = match.soccer_match(random.choice(School.students), random.choice(School.students), School)
#   The following is just a burned part, just for you Miki
user_input = input("match_with_Miki()")
match_with_miki = FoosballMatch()
match_with_miki.match_with_Miki(winner, "Miki")
user_input = input(" School.check_energy()")
energy_level = School.check_energy()
user_input = input("School.do_event_after_school()")
School.do_event_after_school()
user_input = input("School.check_energy()")
energy_level = School.check_energy()
print("See you next day guys")
print("may the beer with you")
