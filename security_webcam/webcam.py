"""
will access camera device and record video footage
and will save them in files.
"""
import cv2 
from datetime import datetime, timedelta

TIMEOUT = 30

camera = cv2.VideoCapture(2)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') # (*"X264") #(*'XVID')

initial_time = datetime.now()
#out = cv2.VideoWriter(f'{str(initial_time)}.avi',fourcc, 10.0, (640,480))
name = f"video_{initial_time.day}_{initial_time.month}_{initial_time.year}_{initial_time.hour}_{initial_time.minute}.avi"
print(name)
out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))

while True:
    ret, image = camera.read()
    if ret == True:
        image = cv2.flip(image, 1)
        #im = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # or convert
        #equ = cv2.equalizeHist(im) 
        #cv2.imshow('frame_1', equ)
        cv2.imshow('frame_2', image)
        out.write(image)
        
        if datetime.now().timestamp() >= (initial_time + timedelta(minutes=1)).timestamp():
            out.release()
            print("File Saved!")
            initial_time = datetime.now()
            name = f"video_{initial_time.day}_{initial_time.month}_{initial_time.year}_{initial_time.hour}_{initial_time.minute}.avi"
            print(name)
            out = cv2.VideoWriter(name,fourcc, 10.0, (640,480))
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
camera.release()
out.release()
cv2.destroyAllWindows()

