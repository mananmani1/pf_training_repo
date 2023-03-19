import cv2 

def surf_features():
   
    image_name = input("Enter the name of image file with extension: ")
    # reading the image
    img = cv2.imread(image_name)
    # convert to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # create SURF feature extractor
    surf = cv2.SURF_create()

    # detect features from the image
    keypoints = surf.detect(gray, None)
    # draw the detected key points
    # sift_image = cv2.drawKeypoints(img, keypoints, None, (255, 0, 255))
    surf_image = cv2.drawKeypoints(img, keypoints, None, (255, 0, 255))

    # show the image
    cv2.imshow('surf image', surf_image)
    # save the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()

surf_features()