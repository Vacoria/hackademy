# a list is a collection of several objects
# to define a list you have to use square brackets:


a = [1,1,12]

b = ["harry", "hermione", "ron"]

c = [1, "harry", 3.4, "blue"]

#lists can be used also with operators
#lists have sort of index for every position, starting from 0
# to have the name "harry" from b:

print(b[0])
print(len(b))

#to print all the items in the list without the list itself, we can use a for loop
# a for loop allows to iterate for every item in a list one by one and do something with each one of them
# you can write item or ex or whatever you want 
# in this case, for every object in b we print it

for item in b:
    print(item)

for number in a:
    print(number)
    print("ciao")


#exercise1: the loop has to print the number multiplied by 2

d=[1,2,3,4]

for n in d:
    x=n*2
    print(x)

#or, alternatively 

for n in d:
    print(n*2)


#exercise 2: print one number which has to be the sum of all the numbers in the list

total = 0

for m in d:
    total = m + total
    
    
print(total)

# total is called accumulated variable. it is updated every time the for loop is updated


#exercise 3: print one number which is the multiplication of the numbers in the list

g=[12,3,12]
totalm=1
for m in g:
    totalm = m * totalm

print(totalm)

#exercise 4: call the function in code.py, call it in a new way and
import code 
the_sum = code.my_sum(a)
print(the_sum)

# exercise 5: call the function in code.py for products
the_product = code.my_product(a)
print(the_product)

#exercise 6: I have to know how many elements you have in a list
the_count = code.my_count(a)
print(the_count)

#exercise 7: write a function that counts the number of items smaller than 5
the_count_less_than_5 = code.my_count_less_than_5(a)
print(the_count_less_than_5)

#exercise 8: write a function that counts the number of ones in a list
the_count_ones = code.my_count_ones(a)
print(the_count_ones)

#exercise 9: write a function that gives you the max number in a list
the_max = code.my_max(a)
print(the_max)

#exercise 10: write a function that  gives the directory & names of the files in a directory
the_get_filenames = code.get_filenames("C:\\Users\\vale\\Desktop\\")
print(the_get_filenames)


#exercise 11: concept of shallow copy: if you copy a list that has an element which is a list, then the copy you make is actually referring to the list in the list as well.
# example: past it in pythontutor and see the visualization
 
a=[1,2,["ciao", "hi"]]
a[2][1]= "hola" #to change an element of the list which is a list of the list

def play_with_list(a_list):
    print(a_list)
    a_list[0]: "good morning"
    return a_list

def get_list_copy(a_list):
    new_list = []
    for n in a_list:
        new_list.append(n)
    return new_list

print(a)
b=play_with_list(a)
b[1]: "gruezi"

c= get_list_copy(a)
c[0]=6

# -- end of example

#exercise 12: from a list [12, [3,4],36]. print it so that if n is a number, it is printed on a single line; if it is a list, its elements are printed on the same line as numbers
#to print two elements on the same row, you have to use print("ciao", end=" ")

li = [12,34,[56,67], 78]

def print_right(a_list_with_lists):
    for n in a_list_with_lists:
        if isinstance(n,list):
            for i in n:
                print(i, end="")
            print(str())  #print an empty string so the next element is not printed on the same level 
        else: 
            print(n)

print_right(li)

#exercise 13: take a lists with some repeated elements and return a new list that has only single values

#exercise 14: create a function that does the following
 #is_duplicate_there(list_a,list_b)
 #is_duplicate_there( [1,2,3], [4, 5, 1]) --> True
 #is_duplicate_there([1,2,3], [4,5,6]) --> False

def is_duplicate_here(list_a,list_b):
    size_a = len(list_a)
    size_b = len(list_b)
    true_or_false = []
    for e in range(size_a):
        for n in range(size_b):
            if list_a[e] == list_b[n]:
                true_or_false = True
                return true_or_false
            else:
                true_or_false = False 
    return true_or_false = False
    
            
g= [1,2,3] 
k= [4, 5, 6] 

is_duplicate_here(g,k)

        