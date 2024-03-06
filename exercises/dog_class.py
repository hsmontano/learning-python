class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks  = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

count = 0
firu = Dog("Firulais")
while count < 5:
    name = input("Type the dog trick: ")
    firu.add_trick(name)
    count += 1

[print(trick) for trick in firu.tricks]
