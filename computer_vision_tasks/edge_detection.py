import cv2
import numpy as np
from matplotlib import pyplot as plt

def img_edge():
   
    image_name = input("Enter the name of image file with extension: ")
    #read image
    given_image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(given_image, cv2.COLOR_BGR2RGB)

# Applying the Canny Edge filter edge detection

    # thresh_lower = 50  # Lower Threshold
    # thresh_upper = 150  # Upper threshold
    # canny_edge = cv2.Canny(given_image,thresh_lower,thresh_upper)

# Applying the sobel  edge detection
    edgesx = cv2.Sobel(img, -1, dx=1, dy=0, ksize=1)
    edgesy = cv2.Sobel(img, -1, dx=0, dy=1, ksize=1)
    sobel_edges = edgesx + edgesy

# Applying the laplacian  edge detection
    # # first Apply gaussian blur
    # blur_img = cv2.GaussianBlur(given_image, (3, 3), 0)
    # # Laplacian Operator
    # laplacian = cv2.Laplacian(blur_img, cv2.CV_64F)
    


    cv2.imshow('Orignal Image',given_image)
    cv2.imshow('Edge Detection with sobel',sobel_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_edge()