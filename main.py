import cv2
import numpy as np
import pyperclip

img = None
img_size = (960,960)
sample_counter = 0
sample_counter_internal = 1
last_point = None
drawing = False
trajectory = []

def reset():
    global img, last_point, trajectory, sample_counter
    img = np.full((img_size[0], img_size[1], 3) , (255, 255, 255), np.uint8)
    cv2.putText(img, "Press r to reset, c to copy path and esc to exit", (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 170, 50), 1)
    last_point = None
    trajectory = []
    sample_counter = 0  

def on_mouse_moved(event, x, y, flags, param):
    global img, last_point, drawing, trajectory, sample_counter_internal, sample_counter

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            point = (x,y)
            sample_counter += 1
            if sample_counter >= sample_counter_internal:
                cv2.circle(img, (int(point[0]), int(point[1])), 2, (25,25,25), -1)
                if not last_point is None:
                    cv2.line(img, (int(last_point[0]), int(last_point[1])), (int(point[0]), int(point[1])), (0, 255, 0))            
                last_point = point
                trajectory.append(point)
                sample_counter = 0

cv2.namedWindow('simulation_flight_path_creator')
cv2.setMouseCallback('simulation_flight_path_creator', on_mouse_moved)
reset()

while True:
    cv2.imshow('simulation_flight_path_creator', img)
    k = cv2.waitKey(1)
    #if k > 0:
    #    print(f'Key press {k} captured.')
    if k == 27:  # escape
        break
    if k == 99:  # c
        pyperclip.copy(f'super().__init__({img_size},{trajectory})')
    if k == 114:  # r
        reset()
