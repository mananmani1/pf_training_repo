import cv2


def contour_detection():
   
    image_name = input("Enter the name of image file with extension: ")
    # reading the image
    image = cv2.imread(image_name)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    edged = cv2.Canny(blurred, 10, 100)

    cv2.imshow("Original image", image)
    cv2.imshow("Edged image", edged)
    cv2.waitKey(0)

contour_detection()
