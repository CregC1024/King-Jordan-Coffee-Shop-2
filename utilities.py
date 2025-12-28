def welcome():
    print("King Jordan Coffee Shop Simulator 4000, version 1.00")
    print("Copyright 2024 Universal Source Code LLC, All Rights Reserved.\n")
    print("Written by Creg Clarence Sullivan Senior Principal Software Engineer.\n")
    print(" Lets collect some information before we start the game.\n")

    def prompt(display="Please input a string", require=True):
        if require:
            s = False
            while not s:
                s = input(display + " ")
            else:
                s = input(display + " ")
        return s
    
    def convert_to_float(s):
        try:
            f = float(s)
        except ValueError:
            f = 0
        return f
    
    def x_of_y(x, y):
        num_list = []
        # Return a list of x copies y 
        for i in range(x):
            num_list.append(y)
        return num_list