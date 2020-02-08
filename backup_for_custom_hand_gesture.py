import cv2
import numpy as np 

# set to 0, if you use webcam
# otherwise, needs to be replaced with video, update is in development

def nothing(x):
	pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("HSV Trackbars")

cv2.createTrackbar("Lower H", "HSV Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower S", "HSV Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower V", "HSV Trackbars", 0, 255, nothing)

cv2.createTrackbar("Upper H", "HSV Trackbars", 179, 179, nothing)
cv2.createTrackbar("Upper S", "HSV Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper V", "HSV Trackbars", 255, 255, nothing)

cv2.namedWindow("Edges Thresholds")

cv2.createTrackbar("Edge Threshold 1", "Edges Thresholds", 1, 500, nothing)
cv2.createTrackbar("Edge Threshold 2", "Edges Thresholds", 1, 500, nothing)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	l_h = cv2.getTrackbarPos("Lower H", "HSV Trackbars")
	l_s = cv2.getTrackbarPos("Lower S", "HSV Trackbars")
	l_v = cv2.getTrackbarPos("Lower V", "HSV Trackbars")

	u_h = cv2.getTrackbarPos("Upper H", "HSV Trackbars")
	u_s = cv2.getTrackbarPos("Upper S", "HSV Trackbars")
	u_v = cv2.getTrackbarPos("Upper V", "HSV Trackbars")

	threshold_1 = cv2.getTrackbarPos("Edge Threshold 1", "Edges Thresholds")
	threshold_2 = cv2.getTrackbarPos("Edge Threshold 2", "Edges Thresholds")


	lower_col = np.array([l_h, l_s, l_v])
	upper_col = np.array([u_h, u_s, u_v])
	mask = cv2.inRange(hsv, lower_col, upper_col)
	median = cv2.medianBlur(mask, 15)
	median2 = cv2.medianBlur(median, 15)

	res = cv2.bitwise_and(frame, frame, mask=median2)
	#median = cv2.medianBlur(res, 15)

	result = cv2.bitwise_and(frame, frame, mask=mask)
	#median2 = cv2.medianBlur(mask, 15)

	edges_from_res = cv2.Canny(res, threshold_1, threshold_2)
	edges_from_result = cv2.Canny(res, threshold_1, threshold_2)

	#edge_res = cv2.bitwise_and(frame, res, mask=median2)

	cv2.imshow("frame", frame)
	#cv2.imshow("mask", mask)
	cv2.imshow("result", result)
	cv2.imshow("res", res)
	#cv2.imshow("median", median)
	cv2.imshow("median2", median2)
	cv2.imshow("edges", edges_from_res)
	cv2.imshow("edges_from_result", edges_from_result)

	key = cv2.waitKey(1)

	# if ESC
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()