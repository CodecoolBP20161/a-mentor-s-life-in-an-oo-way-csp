class Person:
    possible_genders = ["male", "female", "not sure"]

    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, happiness_level):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        if gender not in self.possible_genders:
            raise ValueError("Genders: male, female, not sure")
        else:
            self.gender = gender
        self.energy_level = energy_level
        self.happiness_level = happiness_level

    def gym(self):
        if self.energy_level < 100:
            self.energy_level += 30
            if self.energy_level > 100:
                self.energy_level = 100
