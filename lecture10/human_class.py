
class Human:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work


class Engineer:
    def __init__(self, name, age, designation, work, qualification, salary):
        self.name = name
        self.age = age
        self.work = work
        self.designation = designation
        self.qualification = qualification
        self.salary = salary


class Doctor:
    def __init__(self, name, age, speciality, qualification, experience):
        self.name = name
        self.age = age
        self.speciality = speciality
        self.qualification = qualification
        self.experience = experience


class Carpenter:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience


class Teacher:
    def __init__(self, name, age, experience, speciality, qualification):
        self.name = name
        self.age = age
        self.experience = experience
        self.speciality = speciality
        self.qualification = qualification

h1 = Human(name="ABC", age=33)
h2 = Human(name="XYZ", age=2)
