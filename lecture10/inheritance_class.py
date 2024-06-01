
class Human:        # Base class or Parent Class
    _name = "ABC"
    age  = 33

    def speak(self):
        print("Hello My name is ", self._name)

class Engineer(Human):      # Derived class or Child class
    speciality = "Software"


class Doctor(Human):        # Derived class or Child class
    qualification = "MBBS"

e = Engineer()
d2 = Doctor()

print(e._name)
# print(e.speciality)
# e.speak()


# print(d2._name)
# print(d2.qualification)


class CivilEngineer(Engineer):      # Example of Multi-level inheritance
    pass