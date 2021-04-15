from Pets_Home_Class import Pets


class Cats(Pets):

    def __init__(self, name="", residence_place=""):
        super().__init__()
        self.name = name
        self.resident_place = residence_place


cat_one = Cats()
cat_one.animal_kind = "Cat"
cat_one.name = "Snowman"
cat_one.age = 15
cat_one.sex = "male"
cat_one.breed = "Brit"
cat_one.residence_place = "Homeless"

print("Kind of animal : ", cat_one.animal_kind)
print("Name : ", cat_one.name)
print("Breed : ", cat_one.breed)
print("Sex : ", cat_one.sex)
print("Age : ", cat_one.age)
print("Place of residence : ", cat_one.residence_place)
