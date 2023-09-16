# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import mediapipe as mp
import argparse
import imutils
import cv2
import pandas as pd



# mediapip initialize
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      model_complexity = 0,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())


# img = cv2.imread('C:/Users/akmal/OneDrive/Pictures/No Mans Sky/img.png')

# cv2.imshow('image', img)
#define the events for the
# mouse_click.
def mouse_click(event, x, y, flags, userdata: int):

      
	# to check if left mouse 
	# button was clicked
	if event == cv2.EVENT_LBUTTONDOWN:
		# font for left click event
		print("clicked",userdata)
		action[userdata] = 1
          
          
    # to check if right mouse 
    # button was clicked
	if event == cv2.EVENT_RBUTTONDOWN:
           
        # font for right click event
		font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
		RB = 'Right Button'
		  
		# display that right button 
		# was clicked.
		cv2.putText(img, RB, (x, y),
		            font, 1, 
		            (0, 255, 255),
		            2)
		cv2.imshow('image', img)

  
# cv2.setMouseCallback('image', mouse_click)
   
# cv2.waitKey(0)
  
# close all the opened windows.
# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter

print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()
x= []
y=[]
z=[]
n = 500
action = [0] * n
# loop over some frames...this time using the threaded stream

while len(x)<n:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	results = hands.process(imgRGB)
	ln = len(x)
	print(ln)
	# cv2.setMouseCallback("Frame", click_event)
	# frame = imutils.resize(frame, width=400)
	# results = hands.process(imgRGB)
	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		# cv2.namedWindow("Frame")
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

	

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id, lm in enumerate(handLms.landmark):
				if id == 8:
				  #print(id,lm)
				  h, w, c = frame.shape
				  cx, cy = int(lm.x *w), int(lm.y*h)
				  x.append(cx)
				  y.append(cy)
				  z.append(lm.z)
				  cv2.setMouseCallback('Frame', mouse_click, ln)
				
	# 			  print(cx,cy,cz)
	# 			  #if id ==0:
	# 			  cv2.circle(frame, (cx,cy), 3, (255,0,255), cv2.FILLED)
    # cv2.imshow("Frame", frame)

	# update the FPS counter
	fps.update()
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
data = {'x':x,'y':y,'z':z, 'action':action}
print('length of action', len(action))
df = pd.DataFrame(data)
print(df.shape)
df.to_csv('clicks.csv', sep=',')
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()