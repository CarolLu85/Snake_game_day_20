# class inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()


    def breathe(self):
        super().breathe()
        print("doing this underwater")



    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()

# in this case, Animal class is the super class, via using "super().__init__（）"
# everything in Animal class is imported to Fish class.
