class character:

    def character(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("I'm {}".format(self.name))
        print("My age is {}".format(self.age))


# #別々のインタプリタを定義
# charaA = character()
# charaB = character()

# charaA.character("Aoi", 19)
# charaB.character("Nozomi", 35)
# #それぞれのインタプリタ変数は違う値を保持している
# charaA.introduce()
# charaB.introduce()