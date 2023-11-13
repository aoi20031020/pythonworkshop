class Sample:

    #初期化処理
    def __init__(self):
        self.a = 0
        self.b = 0

    def sum(self):
        return self.a + self.b
    
    def num(self, a, b): 
        self.a = a
        self.b = b

data = Sample() 
print(data.sum())
data.num(3, 7) 
print(data.sum()) 


