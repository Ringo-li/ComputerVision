import cv2
import os

print(os.listdir("./"))
CWD = os.path.dirname(os.path.abspath(__file__))
os.chdir(CWD)
print(os.listdir("./"))

img = cv2.imread('./img/cat.jpg')
while True:
    cv2.imshow('cat', img) 
    # if cv2.waitKey(10) & 0xFF == 27:
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()