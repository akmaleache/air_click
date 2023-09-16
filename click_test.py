# import cv2

# image = cv2.imread("C:/Users/akmal/OneDrive/Pictures/No Mans Sky/img.png")
# imS = cv2.resize(image, (300, 150))

# cv2.namedWindow("image")

# cv2.imshow('image', imS)
# cv2.waitKey(0)
# def click_event(event, x, y, flags, param):
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		print('clicked')
# 		action.append(1)
# 	elif event == cv2.EVENT_LBUTTONDBLCLK:
# 		action.append(2)
# # cv2.destroyWindow("image")
# cv2.setMouseCallback('image', click_event)
# cv2.destroyAllWindows()
# cv2.waitKey(0)

# from pynput.mouse import Listener
# def click(x,y,button,pressed):
#     # print("Mouse is Clicked at (",x,",",y,")","with",button)
#     print("click")
# with Listener(on_click=click) as listener:
#     listener.join()

import cv2
  
  
# read image
img = cv2.imread('C:/Users/akmal/OneDrive/Pictures/No Mans Sky/img.png')
# img_re = cv2.resize(img, (300, 150))

# cv2.namedWindow("image")

# cv2.imshow('image', imS)
# show image
cv2.imshow('image', img)
#define the events for the
# mouse_click.
def mouse_click(event, x, y, 
                flags, param):
      
    # to check if left mouse 
    # button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
          
        # font for left click event
        font = cv2.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'
          
        # display that left button 
        # was clicked.
        cv2.putText(img, LB, (x, y), 
                    font, 1, 
                    (255, 255, 0), 
                    2) 
        cv2.imshow('image', img)
          
          
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
  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)
  
# close all the opened windows.
cv2.destroyAllWindows()