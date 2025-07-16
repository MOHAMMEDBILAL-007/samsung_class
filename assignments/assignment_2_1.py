class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name is {self.name}"

p = Person("Alice")
print(p)  # Calls __str__
