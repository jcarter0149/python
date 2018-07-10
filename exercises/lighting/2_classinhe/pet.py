

class Pet():
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def set_owner(self, owners_name):
            self.owners_name = owners_name
            
    def __str__(self):
        return f'this pets name is {self.name}. It has {self.animal_type.leg_num} legs and likes to say {self.animal_type.say_something()}'

