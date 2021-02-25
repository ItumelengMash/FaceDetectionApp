import cv2

img = cv2.imread("jcole.jpg", 1)


resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("GOAT", resized)

cv2.waitKey(5000)

cv2.destroyAllWindows()

