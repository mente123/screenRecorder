import cv2
import  numpy as np
from PIL import ImageGrab

def screenRecorder():
    fource = cv2.videowriter_fourcc(*'XVID')
    out = cv2.videowriter("output.avi", fourcc, (1360, 768))  # putting the resolution of the computer to get saved the video in compatible way
    
    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        # open cv color format is bgr format so we will change to rgb color format
        
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        
        cv2.ieshow("screen recorder", frame)
        
        out.write(frame)
        
        if cv2.waitKey(1) == 27:
            break
    out.release()
    cv2.destroyAllWindows()
    
screenRecorder()