import cv2
import numpy as np

# This file has implementation for Background Reduction procedure,
# that leave only specific range of colors present in the scene

# Modify pop-up trackbars, in order to set different color ranges

# set to 0, if you use webcam
# otherwise, needs to be replaced with video, update is in development

def nothing(x):
	pass

# Setting up 2 track bars
# one for HSV coloring filter
cv2.namedWindow("HSV Trackbars")

# default values, found to be the best
# Min (H:0, S:0, V:70)
# Max (H:37, S:128, V:255)

cv2.createTrackbar("Lower H", "HSV Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower S", "HSV Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower V", "HSV Trackbars", 70, 255, nothing)

cv2.createTrackbar("Upper H", "HSV Trackbars", 37, 179, nothing)
cv2.createTrackbar("Upper S", "HSV Trackbars", 128, 255, nothing)
cv2.createTrackbar("Upper V", "HSV Trackbars", 255, 255, nothing)

# another for Edgest Threshold amount
cv2.namedWindow("Edges Thresholds")

cv2.createTrackbar("Edge Threshold 1", "Edges Thresholds", 1, 500, nothing)
cv2.createTrackbar("Edge Threshold 2", "Edges Thresholds", 1, 500, nothing)


# capturing from video camera
cap = cv2.VideoCapture(0)

#######################
while True:

	# reading frame by fram from capturing device
	_, frame = cap.read()

	# converting each fram color from BGR into HSV
	# HSV is good for skin coloring and color filtering
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# lower values for Hue, Saturation, and Value of HSV
	# they are used to create a lowest range of colors that we allow in image
	l_h = cv2.getTrackbarPos("Lower H", "HSV Trackbars")
	l_s = cv2.getTrackbarPos("Lower S", "HSV Trackbars")
	l_v = cv2.getTrackbarPos("Lower V", "HSV Trackbars")

	# higher values for Hue, Saturation, and Value
	# they are used to create a highest range of colors that we allow in image
	u_h = cv2.getTrackbarPos("Upper H", "HSV Trackbars")
	u_s = cv2.getTrackbarPos("Upper S", "HSV Trackbars")
	u_v = cv2.getTrackbarPos("Upper V", "HSV Trackbars")


	# Separate values for another track bar, which is used for Edge thresholds
	# this lets us to balance between amount of edges being captured and seen in the video feed
	threshold_1 = cv2.getTrackbarPos("Edge Threshold 1", "Edges Thresholds")
	threshold_2 = cv2.getTrackbarPos("Edge Threshold 2", "Edges Thresholds")



	# converting received images into numpy array, in order to feed into mask function
	lower_col = np.array([l_h, l_s, l_v])

	# same as a line above, but with upper values from trackbar
	upper_col = np.array([u_h, u_s, u_v])

	# Good values found HSV values for light skin:
	# Min (H:0, S:0, V:104)
	# Max (H:32, S:114, V:255)

	# And:
	# Min (H:0, S:0, V:55)
	# Max (H:37, S:120, V:255)

	# And:
	# Min (H:0, S:0, V:0)
	# Max (H:30, S:137, V:255)

	# BEST:
	# And:
	# Min (H:0, S:0, V:70)
	# Max (H:37, S:128, V:255)


	# creating output filters based on HSV's allowed ranges

	# ///////////////////////////
	# this is a preparation for what would be used for final filtering results:
	# simple mask, black & white image
	mask = cv2.inRange(hsv, lower_col, upper_col)
	# median has less noise compared to 
	median = cv2.medianBlur(mask, 15)
	# creating another blur, but blurring the median blur, to get even better noise reduction
	median2 = cv2.medianBlur(median, 15)
	# ////////////////////


	# ////////////////////
	# these are final results that now reduce the noise from original mask and median blur feed
	res = cv2.bitwise_and(frame, frame, mask=median2)
	h, s, v_gray_res = cv2.split(res)
	#edges_from_res = cv2.Canny(res, threshold_1, threshold_2)
	# /////////////////////


	# original base of feed filters
	cv2.imshow("frame", frame)
	#cv2.imshow("median", median)
	#cv2.imshow("median2", median2)

	# clean, final version of filtering
	#cv2.imshow("res", res)
	#cv2.imshow("v_gray_res", v_gray_res)
	# not sure if edges is a good choice
	#cv2.imshow("edges", edges_from_res)


	# read frames until "Esc" is hit
	key = cv2.waitKey(1)

	# if ESC
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()