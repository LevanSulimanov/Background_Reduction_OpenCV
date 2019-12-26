import cv2
import numpy as np 

# set to 0, if you use webcam
# otherwise, needs to be replaced with video, update is in development

def nothing(x):
	pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("YCrCb Trackbars")

cv2.createTrackbar("Lower Y", "YCrCb Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower Cr", "YCrCb Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower Cb", "YCrCb Trackbars", 0, 255, nothing)

cv2.createTrackbar("Upper Y", "YCrCb Trackbars", 179, 179, nothing)
cv2.createTrackbar("Upper Cr", "YCrCb Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper Cb", "YCrCb Trackbars", 255, 255, nothing)

while True:
	_, frame = cap.read()
	YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)


	l_Y = cv2.getTrackbarPos("Lower Y", "YCrCb Trackbars")
	l_Cr = cv2.getTrackbarPos("Lower Cr", "YCrCb Trackbars")
	l_Cb = cv2.getTrackbarPos("Lower Cb", "YCrCb Trackbars")

	u_Y = cv2.getTrackbarPos("Upper Y", "YCrCb Trackbars")
	u_Cr = cv2.getTrackbarPos("Upper Cr", "YCrCb Trackbars")
	u_Cb = cv2.getTrackbarPos("Upper Cb", "YCrCb Trackbars")


	lower_col = np.array([l_Y, l_Cr, l_Cb])
	upper_col = np.array([u_Y, u_Cr, u_Cb])
	mask = cv2.inRange(YCrCb, lower_col, upper_col)

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