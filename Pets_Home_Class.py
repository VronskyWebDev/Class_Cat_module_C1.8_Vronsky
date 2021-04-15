class Pets:
    def __init__(self, animal_kind="", breed="", sex="", age=""):
        self.animal_kind = animal_kind
        self.breed = breed
        self.sex = sex
        self.age = age

    def get_animalkind(self):
        return self.animal_kind

    def get_breed(self):
        return self.breed

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

