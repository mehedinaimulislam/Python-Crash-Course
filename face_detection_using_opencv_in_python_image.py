# import the necessary libraries
import cv2

# Load the image
image = cv2.imread("image.jpg")

# Convert the image to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Detect faces in the grayscale
faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5,
                                      minSize=(30, 30))
"""
=> 'gray_image': the graysclae image to be searched for faces. 
=> 'scaleFactor': the factor by which the image size is reduced at each image 
sclae must have to be retained. 
=> 'minSize': the minimum size of the face rectangle.
"""

# draw rectangel
for (top, left, bottom, right) in faces:
    cv2.rectangle(image, (top, left), (top + left, bottom + right), (0, 255, 0), 2)

# display the image
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
