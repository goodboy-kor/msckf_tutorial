import cv2
import os

# path = "./data/mav0-2/cam0/data/1403636579763555584.png"
path = "./data/img/a.jpg"

img = cv2.imread(path, cv2.IMREAD_COLOR)

original = cv2.imread(path, cv2.IMREAD_COLOR)
gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(path, cv2.IMREAD_UNCHANGED)

cv2.imshow('Original', original)
cv2.imshow('Gray', gray)
cv2.imshow('Unchange', unchange)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


k = cv2.waitKey(0)
if k == 27:  # esc key
    cv2.destroyAllWindows()
elif k == ord('s'):  # 's' key
    cv2.imwrite('./data/img/img.png', img)
    cv2.imwrite('./data/img/gray.png', gray)
    cv2.imwrite('./data/img/unchange.png', unchange)
    cv2.destroyAllWindows()
