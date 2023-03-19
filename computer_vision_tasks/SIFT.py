import cv2 

def sift_features():
   
    image_name = input("Enter the name of image file with extension: ")
    # reading the image
    img = cv2.imread(image_name)
    # convert to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # create SIFT feature extractor
    sift = cv2.SIFT_create()

    # detect features from the image
    keypoints = sift.detect(gray, None)
    # draw the detected key points
    # sift_image = cv2.drawKeypoints(img, keypoints, None, (255, 0, 255))
    sift_image = cv2.drawKeypoints(img, keypoints, None, (255, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS  )

    # show the image
    cv2.imshow('image', sift_image)
    # save the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()

sift_features()