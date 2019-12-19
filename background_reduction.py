import cv2
import numpy as np 

# set to 0, if you use webcam
# otherwise, needs to be replaced with video, update is in development

def background_reduction():

	cap = cv2.VideoCapture(0)
	fgbg = cv2.createBackgroundSubtractorMOG2()

	while True:
		ret, frame = cap.read()
		fgmask = fgbg.apply(frame)
		#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		#lower_red = np.array([0, 0, 0])
		#upper_red = np.array([150, 150, 150])

		#mask = cv2.inRange(hsv, lower_red, upper_red)
		#res = cv2.bitwise_and(frame, frame, mask = mask)

		cv2.imshow('original', frame)
		#cv2.imshow('frame', frame)
		#cv2.imshow('mask', mask)
		#cv2.imshow('res', res)
		cv2.imshow('fg', fgmask)

		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break

	cv2.destroyAllWindows()
	cap.release()

background_reduction()