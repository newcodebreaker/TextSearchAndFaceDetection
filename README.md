# Face detection and text search in images

This is a face detection project in Python3 wherein we perform a text search on an image file and if the text is present in the image, we detect all the faces in that image, crop them and paste on a canvas for display.


## Input
The input is provided in the form of a zipper folder that contains the image files


## Algorithm:

Step 1: Import libraries zipfile.ZipFile, PIL, PIL.image, PIL.ImageDraw, pytesseract, cv2, numpy and os  
Step 2:  Load the face detection classifier “haarcascade_frontalface_default.xml”  from cv  
Step 3:  Read the zip folder containing the images  and open all the image files in that folder one by one  
Step 4:  Extract the zipped files inside a chosen directory  
Step 5:  Convert all the image files into RGB mode  
Step 6:  Search for a sample text (like ‘Christopher’) using pytesseract.image_to_string(image_file)  
Step 7:  If the searched text is present in the image file, start face detection   
Step 8:  For face detection in the image file, first read the image file using cv.imread(filenname) and pass it to the face detection classifier loaded in step 2  
Step 9:  The face detection classifier returns a list of the bounding box of the faces in the form of x(upper left x-coordinate), y(upper left y-coordinate), w(width of the image), h(height of the image)  
Step 10: Calculate the total number of faces found in the image file, along with the maximum width and maximum height of the faces  
Step 11 : Calculate the total number of rows of faces needed for pasting on a contact_sheet, with five faces per row    
Step 12: Create a contact_sheet for pasting the cropped faces using the number of rows needed calculated in step 11 and maximum height and width of faces found in step 10 as the dimensions of each face  	
Step 13: Iteratively crop the faces using filename.crop(faceArea), where faceArea is a tuple of bounding boxes found in step 9, and paste it on contact_sheet created in step 12  


## Output
A canvas containing the cropped faces detected in the image





