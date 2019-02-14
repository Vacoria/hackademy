

#let's set up the game of life structure
import random 

def setup_game(size, max_alive):
    empty_grid = get_empty_grid(size)  #to create the grid, we have to instruct on the size aka the dimension of the grid
    fill_grid_random(a_grid, max_alive)

def get_empy_grid(size): 
    new_grid=[]
    for row in range(size):
        new_sublist= []
        for column in range(size):
            new_sublist.append('-')
        new_grid.append(new_sublist)
    return new_grid

def rand_alive(): #to get number of alive cells, number is cosen randomly
    number = random.randint(1,3) #it gives number between 1 and 3 excluded, thus either 1 or 2
    if number == 1:
        return True
    else:
        return False 

def fill_grid_random(a_grid,max_alive):
    size = len(a_grid)
    remaining = max_alive 
    for r_i in range(size):
        for c_i in range(size): 
            if remaining > 0: #lo devo mettere qui perche passo sempre da questo punto. se lo metto sopra rimango nel loop senza fermarmi
                if rand_alive() == True:
                    a_grid[r_i][c_i] = 'X'
                    remaining = remaining - 1 # no return!!!!
                else:
                    a_grid[r_i][c_i] = '-'

a = [['-','-','-'],['-','-','-'],['-','-','-']]

fill_grid_random(a,3)

print(a)



# take a, return no list but just three rows with all the elements alligned
# like: 
# --X
# -X-
# -X-

def print_grid(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size): 
            print(a_grid[r_i][c_i], end=" ")
        print(" ")

print_grid(a)



