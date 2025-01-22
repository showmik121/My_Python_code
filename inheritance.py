class User:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def login(self):
        print(f"{self.name} logged in!")

    def register(self):
        print(f"{self.name} registered!")


class Student(User):
    def __init__(self, name, gender, roll):
        super().__init__(name, gender)  # Initialize parent class attributes
        self.roll =roll

    def enroll(self):
        print(f"Student {self.name} with roll {self.roll} enrolled!")


class Instructor(User):
    def __init__(self, name, gender, id):
        super().__init__(name, gender)  # Initialize parent class attributes
        self.id = id

    def create(self):
        print(f"Instructor {self.name} with ID {self.id} created the course!")


# Creating objects and testing functionality
obj = User("Showmik", "Male")
obj.login()
obj.register()

s = Student()
s.login()
s.enroll()
s.name()
