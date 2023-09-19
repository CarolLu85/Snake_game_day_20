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

# list slicing
list = [1,2,3,4,5,6,7,8]
tuple = (1,2,3,4,5,6,7,8)
sliced_list = list[1 : ] this means from the second one to the last.
or
sliced_list = list[ : 6] this means from the beging to the 5th(index)

sliced_list = list[2 : 5 :2]this means from index2 to index 4, everything second number goes to the sliced_list
sliced_list = list[ : : -1] this one reverse the whole list, and this also works on tuples.
sliced_tuple = tuple[2 : 5]