class Events:
    def __init__(self, name, delta_happiness_level, delta_energy_level):
        self.name = name
        self.delta_happiness_level = delta_happiness_level
        self.delta_energy_level = delta_energy_level

    @classmethod
    def create_by_csv(cls, text_file):
        return_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                return_list.append(cls(*row))
        return return_list
