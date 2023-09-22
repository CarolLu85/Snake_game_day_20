# Snake_game_day_20

i still havent had the mindset or logic that store datas in dictionary or list or tuple. 
like this task, at the beginning, to deal with the x and y coordinates, the fisrt thing came up my mind
was just set up two variables (x,y), and change x's value inside the loop.
instead of doing this, i could just figure out the exact x coordinates for all three squares, and save 
their coordinates into a tuple. 

day_24 notes

# to open the text file and read it. via print it, you get to see what is written inside this txt file.
with open("FILENAME.EXTENSION") as VARIABLE(you name it yourself):
    contents = variable.read()
    print(contents)

# to write into a txt file.
with open("FILENAME.EXTENSIION", MODE = "a"/"w"/"r") as VARIABLE:
    variable.write("contents that you wish to write into this txt file")
a = append, r(default) = read, w = write
# if this txt file doesnt exist, using this "with open() as " it gets created automatically. 
