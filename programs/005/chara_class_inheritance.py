class character:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("I'm {}".format(self.name))
        print("My age is {}".format(self.age))

class Aoi(character):

    def __init__(self, name, age, birthday):
        super().__init__(name, age)
        self.birthday = birthday

    def introduce(self):
        super().introduce()
        print("My birthday is {}".format(self.birthday))


charaA = Aoi("Aoi", 19, "2003/10/20")

charaA.introduce()