def hello(a_name):
   print("Hello! " + a_name)


def hello2(name_a, name_b):
   print("Hello! " + name_a + " and " + name_b)


def sum_two(x,y):
   z =x + y 
   return z

#compute area of a circle given the radius, without defining the value of greek py yourself
import math
def circle_area(radius):
   y = math.pi * radius * radius
   return y

print(circle_area(3))

#function that gives me the day of today, namely 11th of february
import datetime
print(datetime.datetime.today().day)
print(datetime.datetime.today().weekday())

#write a function that does the same as the for loop wirtten in loops.py. in this way, we can have the return
def my_sum(a_list):
   total=0
   for n in a_list:
      total= n + total
   return total

#write a function that does the same as the for loop ... for products
def my_product(a_list):
   total=1
   for m in a_list:
      total= total* m
   return total

#write a function that counts the number of items in a list
def my_count(a_list):
   count = 0
   for c in a_list:
      count = 1 + count
   return count
#tip: you don't have to use the c element in the loop compulsorly!!

#write a function that counts the number of items smaller than 5
def my_count_less_than_5(a_list):
   count= 0
   for c in a_list:
      if c < 5:
         count = 1 + count
   return count

#write a function that counts the number of ones in a list
def my_count_ones(a_list):
   count = 0
   for c in a_list:
      if c==1:
         count = 1 + count
   return count

#write a function that gives you the maximum value in a list
# first write the following, as if the list is empty the second function does not work
def is_list_empty(a_list):
   if my_count(a_list) == 0:
      return True
   else:
      return False 

def my_max(a_list):
   if is_list_empty(a_list): #if the list is empty this is true, thus you have none as it stops everything
      return None 
   else: 
      value = a_list[0] #in this way, even if negative number, it works as you just take the first number in the list, not a specific value
      for c in a_list:
         if c > value: 
            value = c
   return value



##write a function that gives you the list [] of  the complete names of the files in a directory ("C:\\Users\\vale")
# interesting function in os package: append adds an element to a list. you have to write: NAMEOFLIST.append("new element to add")
import os
def get_filenames(a_directory):
   list_of_files = os.listdir(a_directory)
   print("list of file names: ")
   print(list_of_files)
   print("---------------")
   all_files = [] #prepare an empty list
   for filename in list_of_files:
      full_path = os.path.join(a_directory, filename) #it is used to merge the name and the path, adding the right sleshes regardless of windows or mac os
      if not os.path.isdir(full_path): #it is needed to avoid having pure directories and not files 
         all_files.append(full_path)
   return all_files 


# grid. imagine you have a list like this [12,34,[56,67]] --> i want  the following output: [12 34 56 67]. 
#let's call the function flatten. TIP: THIS FUNCTION WORKS ONLY FOR LISTS IN LISTS, DOESNT WORK FOR LISTS IN LISTS IN LISTS 
def flatten(a_list_of_lists):
   new_list = [] 
   for n in a_list_of_lists:  
      if isinstance(n,list): #needed, as if n is a list it is just copied and pasted as the original one but with the link to the original list in the list
         for i in n: 
            new_list.append(i) #it appends the element i of the list of the list
      else:
         new_list.append(n)
   return new_list

#to print two elements on the same row, you have to use print("ciao", end=" ")
#to repeat something n times, use range(number of times) and use a for loop. tip: if you put range(3), it uses 0,1,2

#function to print as many starts as you specify in the same row
def single_row_stars(number):
   for n in range(number):
      print("*", end="")

#function to print as many stars and slash as you specify in the same row
def single_row_starsandslash(number):
   for n in range(number):
      print("*/",end="")

#function to print input as many times as you give as you specify in the same row
def single_row_of(number,string):
   for n in range(number):
      print(string, end="" )
     
#function to print n starts per x rows
def rectangle_of_stars(rows, cols):
   for n in range(rows):
      for s in range(cols):
         print("*", end="")
      print()

#function to print the square of n stars (n x n)
def square_of_stars(number):
   for n in range(number):
      for n in range(number):
         print("*", end="")
      print()

#function that takes a list, and returns a new list with the elements multiplied by 2
def list_by_2(a_list):
   new_list=[]
   for n in a_list: 
      new_list.append(n*2)
   return new_list


#function that takes a lists and returns a new list with the elements in reverse order
def list_reverse(a_list):
   new_list= []
   for n in a_list:
      
   
#function that creates a grid with the size you want, thus a list with a list of "-"

def create_grid(size):
   new_grid=[]
   for row in range(size):
      new_sublist= []
      for column in range(size):
         new_sublist.append('-')
      new_grid.append(new_sublist)
   return new_grid


#iteration on lists
# take a list a= ["xx", "ee", "fff"]
# take its length: leng(a) = 3 
# substitute values with iterations

for i in range(len(a)):
   a[i]="rrr"

# if I have a lists of lists, I need two indexes! 
# to print the indexes:
# take a grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'] ]
# grid [1][1] ='x'
# size = len(grid)

for r_i in range(size):
   for c_i in range(size):
      print("r_i = "+ str(r_i), end=" ")
      print("c_i = "+ str(c_i))

# to iterate on square grids and substitute values

for r_i in range(size):
   for c_i in range(size):
      grid[r_i][c_i] = 'X'