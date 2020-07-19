
from zipfile import ZipFile

import PIL
from PIL import Image
from PIL import ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
import os


# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


# read the zipfile
filename= 'readonly/small_img.zip'
print(filename)

# extract image and store it in an array
with ZipFile(filename,'r') as f:
    f.extractall('readonly/sample1/')
#     for item in f:
#         print(item)

# infile  = 'readonly/sample1'
# for item in infile:
#     print(item)

# print the name of the files inside readonly/sample1
# files is a list of all the files which are under sample1 directory
files = os.listdir('readonly/sample1')
print(files)

# display the images one by one
for item in files:
    print("File_name: ", item)
    pil_img=PIL.Image.open('readonly/sample1/'+item)
    # convert the image file to RGB mode
    pil_img = pil_img.convert("RGB")
    #print(pil_img.mode)
    #display(pil_img)


# search for a sample name in the images
name = 'Christopher'

for item in files:
    # current file name read
    print("File currently opening: ", item)

    # open the file name
    pil_img=Image.open('readonly/sample1/'+item)

    # convert it to RGB mode
    pil_img = pil_img.convert("RGB")

    # read the image file for the text in it, this process may toke several minutes
    print("Reading the file {} for text...".format(item))
    text = pytesseract.image_to_string(pil_img)

    print("Reading the file {} for text finished successfully...".format(item))

    # print sample text, first 10 characters
    #print(text[:10])

    # search for the given name in the text as read from the image
    if name in text:
        title = "Results found in file: "
        print(title + "  " + item)

        # now read faces in that image
        print("Reading the file... ", item)
        cv_img=cv.imread('readonly/sample1/'+item) # imread needs path not file name

        print("File {} successfully read...".format(item))

        
        print("Face detection in progress ---")
        # faces is a list of x,y,w,h denoting the bounding box of the faces
        faces = face_cascade.detectMultiScale(cv_img)

        # find number of faces
        numFace = len(faces)
        
        print("Number of faces detected are: ", numFace)
        if numFace == 0:
            print("But there were no faces in that file!")
            continue

        # find the maximum width and height of image in the found images
        maxWidth = 0
        maxHeight = 0
        for x,y,w,h in faces:
            if w > maxWidth:
                maxWidth = w
            if h > maxHeight:
                maxHeight = h
        
        maxWidth = int(maxWidth)
        maxHeight= int(maxHeight)
        print("maxWidth: {}  maxHeight {}". format(maxWidth,maxHeight))

        # number of rows of images needed = total images/5 +1
        rows= 0
        if numFace % 5 == 0:
            rows = numFace / 5
        else:
            rows = int(numFace // 5) + 1   #typecasting to int required from float
        
        rows = int(rows)
        print("Total Number of rows of contact_sheet required: ", rows)
        #PIL.Image.new('RGB', (first_image.width, first_image.height + 50), color = (0,0,0))

        # create a contact_sheet and paste the faces over it found in the image
        contact_sheet=PIL.Image.new('RGB', (5 * maxWidth, (rows * maxHeight) + 60) , color=(0,0,0)) # not "RGB"
        #display(contact_sheet)
        
        # Mistake found! x,y coordinates and x,y,w,h have same name
        x1=0
        y1=0
        count = 0
        for x,y,w,h in faces:
            count += 1
            # crop the image first
            faceArea = (x,y,x+w,y+h)
            face =  pil_img.crop(faceArea)
            display(face)
            contact_sheet.paste(face,(x1,y1))
            if(count%5 == 0):
                y1 = y1 + maxHeight
                x1= 0
            else:
                x1 = x1 + maxWidth
        print("Displaying final contact sheet for ", item)
        display(contact_sheet)
print("Program execution finished...")                
            
