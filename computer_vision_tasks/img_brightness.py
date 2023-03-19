import cv2

def bright_img():
    image_name = input("Enter the name of image file with extension: ")

    img = cv2.imread(image_name)

    # define the alpha and beta
    alpha = 1.5 # Contrast control
    beta = 80 # Brightness control

    # call convertScaleAbs function
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # display the output image
    cv2.imshow('contrast and brightness', adjusted)
    cv2.waitKey()
    cv2.destroyAllWindows()

bright_img()