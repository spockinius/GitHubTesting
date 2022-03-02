class person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = name

    def __str__(self):
        return f"Their name is {self.name} and age is {self.age}."
