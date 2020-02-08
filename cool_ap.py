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

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	l_h = cv2.getTrackbarPos("Lower H", "HSV Trackbars")
	l_s = cv2.getTrackbarPos("Lower S", "HSV Trackbars")
	l_v = cv2.getTrackbarPos("Lower V", "HSV Trackbars")

	u_h = cv2.getTrackbarPos("Upper H", "HSV Trackbars")
	u_s = cv2.getTrackbarPos("Upper S", "HSV Trackbars")
	u_v = cv2.getTrackbarPos("Upper V", "HSV Trackbars")


	lower_col = np.array([l_h, l_s, l_v])
	upper_col = np.array([u_h, u_s, u_v])
	mask = cv2.inRange(hsv, lower_col, upper_col)

	result = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow("frame", frame)
	cv2.imshow("mask", mask)
	cv2.imshow("result", result)

	key = cv2.waitKey(1)

	# if ESC
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()