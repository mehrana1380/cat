class Cat:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def hello(self):
        print("hello may name isn {}".format(self.name))



tadi= Cat("rex",1)

print(tadi.name)
print(tadi.age)
