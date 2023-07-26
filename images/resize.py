# importing the required modules
import os
from PIL import Image
 
# Function to compress the image

def compressimages(image_file):
    # accessing the image file
    filepath = os.path.join(os.getcwd(), image_file)
    # maximum pixel size
    maxwidth = 1200
    # opening the file
    image = Image.open(filepath)
    # Calculating the width and height of the original photo
    width, height = image.size
    # calculating the aspect ratio of the image
    aspectratio = width / height
 
    # Calculating the new height of the compressed image
    newheight = maxwidth / aspectratio
 
 
    # Saving the image
    image.save(image_file, optimize=True, quality=85)
    return


path = os.getcwd()
for file in os.listdir(path):
    if file != "resize.py":
        compressimages(file)

