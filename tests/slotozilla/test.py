class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_text(self):
        print("Hello")


obj = Test("Іван", 25)


class Unit(Test):
    def print_another_text(self):
        print("Python!")


obj2 = Unit("Степан", 33)
obj2.print_text()