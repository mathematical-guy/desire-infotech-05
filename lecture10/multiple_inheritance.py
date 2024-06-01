class Plant:
    grow = "2"


class Food:
    eat = True


class Tomato(Plant, Food, Category):
    color = "red"

t = Tomato()

t.xyz()