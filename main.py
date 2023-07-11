import cv2

# img = cv2.imread("star.jpg")
# print(img.shape)
# img = cv2.resize(img, (100, 100)) #изменение размера картинки
# print(img.shape)

img = cv2.imread("star.jpg")

img = cv2.resize(img, (100, 100))

cv2.imshow('Result', img)

cv2.waitKey(0)
