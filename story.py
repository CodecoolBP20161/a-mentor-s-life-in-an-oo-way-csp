from codecool_class import CodecoolClass


School = CodecoolClass.generate_local()
print("Welcome to Codecool ", School.location + " " + str(School.year))  # print out the welcome text
# user_input = input()

print("The number of students", len(School.students))   # print out the students
print("-"*20)
for i in School.students:
    print(i.first_name + " " + i.last_name)
# user_input = input()

print("\n" + "The number of mentors", len(School.mentors))  # print out the mentors
print("-"*20)
for i in School.mentors:
    print(i.first_name + " " + i.last_name)
# user_input = input()

energy_level_counter = 0
for i in School.students:       # We check the enery level of the students
    energy_level_counter += int(i.energy_level)
energy_level_counter = energy_level_counter//len(School.students)
print("-"*20)
print("\n" + "The average energy level of the class is: " + str(energy_level_counter))
if energy_level_counter < 70:
    print(School.mentors[1].first_name + " " + School.mentors[1].last_name, ':"Class energy is low guys, have a gym"')
    for i in School.students:
        print(i.gym())
for i in School.students:       # We check the enery level of the students again
    energy_level_counter += int(i.energy_level)
energy_level_counter = energy_level_counter//len(School.students)
print("\n" + "The average energy level of the class is: " + str(energy_level_counter))
print(School.mentors[0].first_name + " " + School.mentors[0].last_name, ': "I think that the energy level is optimal"')
# user_input = input()
