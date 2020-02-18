import numpy as np
import cv2
import time
import os

# This program will create labels, based on the label name and number of labels provided
# Uses WebCam as Video Capture, so replace line 22 with whatever fits your needs

# ask what label are we collecting
label = input("Please input name of the label or 'q' to cancel...")
# ask number of samples to collect
frames_to_collect = int(input("How many samples to capture? (Type 0 to cancel) ..."))
# direction to label folder
path = os.getcwd() + "\\train_test_sets\\"

if (label =='q'):
    pass
    
else:
    # start getting video input
    cap = cv2.VideoCapture(0)

    #ready = 'starting...'
    
    # keep looping until we collected specified number of labels
    for i in range(0, frames_to_collect):

        ret, frame = cap.read()

        if ret == None:
            print("Error in Video Feed capture... Exiting...")
            break
        # uncomment to proceed with gray filter
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = frame

        cv2.imshow('frame', gray)
        # saving label
        cv2.imwrite(os.path.join(path, label + "_" + str(int(time.time()))) + ".png", gray)

        time.sleep(1)
        # if you want to quit, press 'q' or 'Esc'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Collection is done, exiting...")
            
    # deallocate all windows and release the webcam
    cv2.destroyAllWindows()
    cap.release()
        