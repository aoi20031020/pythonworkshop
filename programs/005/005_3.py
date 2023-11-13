def equals(num):
    print(num)
def plus(a, b):
    c = a + b
    equals(c)
def minus(a, b):
    c = a - b
    equals(c)
a, b = 60, 30
Re = input("plus or minus: ")
if Re == "plus":
    plus(a, b)
elif Re == "minus":
    minus(a, b) 