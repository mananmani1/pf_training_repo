import cv2
from matplotlib import pyplot as plt


def img_hist():
   
    image_name = input("Enter the name of image file with extension: ")
    given_img = cv2.imread(image_name)
  
    plt.hist(given_img.ravel(),256,[0,256])
    plt.show()
    
    # show the plotting graph of an image
    # plt.plot(histr)
    cv2.imshow('orignal image', given_img)
    # save the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_hist()