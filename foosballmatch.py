import random
from student import Student


class FoosballMatch:
    result = [0, 0]

    def __init__(self):
        self.result = [0, 0]

    def turn_result(self):
        temporary = random.randint(0, 1)
        if temporary == 0:
            self.result[1] += 1
            print("Player two scored")
        else:
            self.result[0] += 1
            print("Player one scored")
        return self.result

    def soccer_match(self, person1, person2, School):
        while person1 == person2:
            person2 = random.choice(School.students)

        print("Player one: " + person1.first_name, person1.last_name)
        print("Player two: " + person2.first_name, person2.last_name)

        while self.result[0] < 6 and self.result[1] < 6:
            self.turn_result()
            print(self.result)
            user_input = input()

        if self.result[0] > self.result[1]:
            print("The winner is: " + person1.first_name + ' ' + person1.last_name)
            print(self.result)
            print("\n")
            return person1

        elif self.result[0] < self.result[1]:
            print("The winner is: " + person2.first_name + ' ' + person2.last_name)
            print(self.result)
            return person2

    def crawl_under_table(self, person):
        print("You sucked it my friend, crawl under the table " + person)
        print(person + ": Ohh noo, I don't want to carwl.☹ ☹ ☹ ")

    def match_with_Miki(self, person1, miki):
        print("\n" + "Miki: I want to challenge the winner"+"\n")
        pressenter = input()
        i = 0
        print("The opponent is:", person1.first_name, person1.last_name)
        while i < 10:
            self.result[0] += 1
            print("Player one scored")
            print(self.result)
            i += 1
            pressenter = input()
        self.crawl_under_table("Miki")
        print("Miki: most meg lettem rakva ...")
        print("\n")
