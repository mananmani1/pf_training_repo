import cv2
import numpy as np
from matplotlib import pyplot as plt


def img_hist():
   
    image_name = input("Enter the name of image file with extension: ")
    given_img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

    # Calculate the pixel frequency
    hist, bins = np.histogram(given_img.ravel(), 256, [0, 256])
    hist1 = cv2.calcHist([given_img],[0],None,[256],[0,256])
    # Set a threshold value
    threshold = 0.01 * np.max(hist)

    # Creating a mask to remove pixels with low frequency in a hieght and width as 
    mask = np.zeros(given_img.shape[:2], dtype=np.uint8)
    for i in range(256):
        if hist[i] < threshold:
            mask[given_img == i] = 255

    # mask
    result = cv2.bitwise_and(given_img, given_img, mask=mask)

    # Display the result
    cv2.imshow('Input Image', given_img)
    cv2.imshow('Output Image', hist1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




    # image_name = input("Enter the name of image file with extension: ")
    # #for color image
    # given_img = cv2.imread(image_name, cv2.IMREAD_COLOR)
   
    # cv2.imshow('Given Image',given_img)
    # hist = cv2.calcHist([given_img],[0],None,[256],[0,256])
    # plt.hist(given_img.ravel(),256,[0,256])
    # plt.title('Histogram for a color picture')
    # plt.show()

    # while True:
    #     k = cv2.waitKey(0) & 0xFF     
    #     if k == 27: break             # ESC key to exit 
    # cv2.destroyAllWindows()

# histogram for rgb's in a given image
    # img = cv2.imread(image_name)
    # color = ('b','g','r')
    # for i,col in enumerate(color):
    #     histr = cv.calcHist([img],[i],None,[256],[0,256])
    #     plt.plot(histr,color = col)
    #     plt.xlim([0,256])
    # plt.show()

img_hist()