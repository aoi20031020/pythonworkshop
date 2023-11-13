class Sample:
    a, b = 0, 0

    def sum(self):
        return self.a + self.b
    
    def num(self, a, b): #引数を変数にセット
        self.a = a
        self.b = b

data = Sample() #インスタンス化
data.num(3, 7) #numメソッド呼び出し
print(data.sum()) #sumメソッド呼び出し


