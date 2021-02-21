class Fruit():
    def __init__(self):
        print("THIS IS A FRUIT")

    def nutrition(self):
        print("FRUITS ARE NUTRITIOUS")

    def fruit_shape(self):
        print("SHAPE......")


#Child class
class orange(Fruit):
    def __init__(self):
        print("THIS IS ORANGE")

#Instance
lk = orange()
lk.nutrition()
lk.fruit_shape()
