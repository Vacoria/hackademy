
#now take the code written in code.py to list the files in a directory and apply it to the function before
import code

# the pillow library is not installed by default in python as it is not part of the python developers products. Check every time for third - party libraries to see the tutorial, go to pillow.readthedocs.io
# pay attention - image has to be written with capital letter
from PIL import Image

# to import the image, you have to copy the path: to do so, go to the graphical interface on the directory, click on the tab and you will see the path. copy and paste it in "" and add a backslash with the name of the file and the extension of the very same. Also, an alternative way is to open the terminal and search for the path of the image: open it and ls the docs in the directory of the picture, you will see the right extension of the picture  #
# remember: put double back slash as a single one has a special meaning in python! 
# to clear the terminal, write clear and enter
im=Image.open("C:\\Users\\vale\\Desktop\\pictures\\picture2.jpg")

# to see the size of the image, just use the function size & print it
# to see the format of the image, use format function: remember that jpg is the short version of jpeg
print(im.size) 
print(im.format)

# to start the appropriate program to show the image, do the following
# tip: if you have any problem, check on the terminal: if there are 3 arrows, it means python is waiting for you.
# close python with control z and do im.show again
im.show()

# select a portion of the image, rotate it and then put it back in the picture
# you can find the tutorial in the session: cutting, pasting etc
# define the box you are focusing on
#define the region you are going to modify
box = (100,100,400,400)
region = im.crop(box)
transposed= region.transpose(Image.ROTATE_180)

# the previous line & in particular the transpose function creates an output which is the copy of the region that is transposed! 
# let's rename this copy "transposed"

im.paste(transposed,box)

#close paint before running the following

im.show()

#in order to apply this to all the images we have, let's create a function. you can write it below the from PIL import ..
#CONSIDER THE SKIPPED PART NOW


# now consider the following: substitute im with an_image, which is the object, and add the return

from PIL import Image
import code

def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed= region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image

# to avoid repeting the codes above for every image, we can use lists --> see loops.py

new_rotational_game = code.get_filenames("C:\\Users\\vale\\Desktop\\pictures\\")
for pic_name in new_rotational_game:
    im = Image.open(pic_name) #you have to first open the image!
    im = rotate_box(im) #you have to torate the im, not everylist
    im.show()

#now i want to change the color of the image to black and white
def to_grayscale(an_image):
    grayscale_im = an_image.convert("L") #iit creates another image, so you have to reassign a new name to it and return that one
    return grayscale_im

# now I want to create a copy of all the images, make it in grey scale and save it in the folder grayscale
import os

new_color_game = code.get_filenames("C:\\Users\\vale\\Desktop\\pictures\\")
num = 0
for pic_name in new_color_game:
    newfilename = "pic_grey_" + str(num) + ".jpg"
    num = num + 1
    im = Image.open(pic_name) #you have to first open the image!
    im = to_grayscale(im) 
    newpathname = os.path.join("C:\\Users\\vale\\Desktop\\pictures\\greyscale\\", newfilename)
    im.save(newpathname)


#VALE FA TORNARE LE IMMAGINI A COLORI E FALLO RI-RUNNARE
