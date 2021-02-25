import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("C:\\Users\\I531157\\Documents\\Extra-Curricula\\PycharmProjects\\FaceDetection"
                                     "\\haarcascade_frontalface_default.xml")

# Reading the image as it is
img = cv2.imread("jcole.jpg")

# Reading the image as gray scale image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=5)

print(faces)
print(type(img))
print(img_gray)

# add rectangular box
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))

#open the resized image in a new window called gray
cv2.imshow("Gray", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()

