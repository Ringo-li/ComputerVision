import cv2
import drawUtils
import time
import os

CWD = os.path.dirname(os.path.abspath(__file__))
os.chdir(CWD)

start_time = time.time()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(img=frame, pt1=(100, 100),pt2=(200,200),color=(255,255,0),thickness=10)
    now = time.time()
    fps_text = int(1/(now-start_time))
    start_time = now
    frame_text = "帧率：" + str(fps_text)
    frame = drawUtils.cv2AddChineseText(frame,frame_text,(20,50),textColor=(0,0,255), textSize=20)
    cv2.imshow("Dome", frame)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

