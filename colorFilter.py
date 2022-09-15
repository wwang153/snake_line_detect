import cv2
import numpy as np

#cap = cv2.VideoCapture(0)

while (1):
    #_, frame = cap.read()
    # It converts the BGR color space of image to HSV color space
    frame = cv2.imread("snake_imgs/00.jpg")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow('raw', hsv)
    # Threshold of blue in HSV space
    lower_red = np.array([30, 50, 50])
    upper_red = np.array([90, 255, 255])

    # preparing the mask to overlay
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # The black region in the mask has the value of 0,
    # so when multiplied with original image removes all non-blue regions
    result = cv2.bitwise_and(hsv, hsv, mask=mask)

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()
