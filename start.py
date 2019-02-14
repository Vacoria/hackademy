import code 
print("Hello!")


a = input ("What is your name?")
b= input ("What is your friend's name?")
code.hello2(a,b)

print(code.circle_area(5))

# the input is a string, thus you have to convert it with the float function: float()#
r= float(input("Give me a radius, please: "))
z= (code.circle_area(r))
print(z)

#if i want to print also "the area is" i have to transform again the variable z as i cannot sum string and float#

print("the area is "+ str(z))

#if i want to ask for a number and print stars accordingly

num = int(input("Give me a number: "))
code.single_row_stars(num)

#print as many stars and an input you give as you specify in the same row

num = int(input("Give me a number: "))
stri = input("tell me your favourite pet: ")
code.single_row_of(num, stri) 

#print the input number of stars you give in a square
code.square_of_stars(4)

#print the input numbers of stars you give in a rectangle

code.rectangle_of_stars(4,2)

# create a new list with function that takes a list, and returns a new list with the elements multiplied by 2
a = [1,2,3]
b= code.list_by_2(a)

# create a new list with function that takes a lists and returns a new list with the elements in reverse order 