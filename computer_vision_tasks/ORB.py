import cv2 

def orb_features():
   
    image_name = input("Enter the name of image file with extension: ")
    # reading the image
    img = cv2.imread(image_name)
   
    # create ORB feature extractor
    orb = cv2.ORB_create()

    # detect features from the image
    keypoints_orb, descriptors = orb.detectAndCompute(img, None)

    # draw the detected key points
    orb_image = cv2.drawKeypoints(img, keypoints_orb, None, (255, 0, 255))

    cv2.imshow('image', orb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

orb_features()