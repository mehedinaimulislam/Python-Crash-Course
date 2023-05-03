import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades
                                     + "haarcascade_frontalface_default.xml")

# To capture video from webcam
capture = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = capture.read()

    # convert to grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect the faces
    faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=4)

    # Draw the rectangle around each face
    for (top, left, bottom, right) in faces:
        cv2.rectangle(img, (top, left), (top + left, bottom + right), (0, 255, 0), 2)

    # display the output
    cv2.imshow("Face Detection", img)

    # stop if escape key is pressed
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

# release the videocapture object
capture.relase()
