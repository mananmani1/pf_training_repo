import cv2
import numpy as np

#most use type of blur (GaussianBlur,medianBlur,Average blurring,bilateralFilter)
def blur_img():
    image_name = input("Enter the path to the image file with extension: ")

    img = cv2.imread(image_name)

    # blur_image = cv2.GaussianBlur(img, (8,8), 0)
    # blur_image = cv2.medianBlur(img,5)
    # ksize = (1,1)
    # blur_image = cv2.blur(img, ksize)
    # blur_image = cv2.blur(src=image, ksize=(75, 75))
    blur_image = cv2.bilateralFilter(img, 5, 100, 100)
    cv2.imshow('Original Image', img)
    cv2.imshow('Blur Image', blur_image)
    cv2.waitKey(0)

blur_img()