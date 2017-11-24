# Part I

def draw_stars(x):
    new_list = []
    for i in range(len(x)):
        b = "*" * x[i]
        print b
 
draw_stars([4, 6, 1, 3, 5, 7, 25])

# Part II

def draw_stars(x):
    new_list = []
    for i in range(len(x)):
        if type(x[i]) == int:
            b = "*" * x[i]
            print b
        elif type(x[i]) == str:
            r = x[i][0].lower()
            print r * len(x)
 
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])