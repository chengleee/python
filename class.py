class Foo:
    
    def __init__(self,name,age):  #是双_，即__init__
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)

obj1 = Foo('chengd',18)
obj1.detail()

obj2 = Foo('ptyhon',99)
obj2.detail()
