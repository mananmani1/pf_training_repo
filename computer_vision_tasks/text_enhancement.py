import cv2


def enhance_text():
    image_name = input("Enter the name of image file with extension: ")
    image = cv2.imread(image_name)
    if image is None:
        print("Error: Failed to load image")
        return

    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    # Apply thresholding for foreground text apprearance so that value may vary on diffent
    adaptive_thresh = cv2.adaptiveThreshold(gray_scale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,71,4)
    # Apply structuring (3x3)
    structuring = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    # Apply morphological operations to remove noise and fill gaps
    eroded = cv2.erode(adaptive_thresh, structuring, iterations=1)


    # Apply median blur filter to further reduce noise
    final_img = cv2.medianBlur(eroded, 1)

    # write any text on  the image
    cv2.putText(final_img, "Enhanced Text by Abdul Manan", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 2, 55), 2)

    cv2.imshow('Enhanced Image', final_img)

    # Save output image
    # cv2.imwrite('output_image.jpg', filtered)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

enhance_text()
