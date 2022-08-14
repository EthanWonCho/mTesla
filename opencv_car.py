import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    ret, img = cap.read() # img 이미지 ret 부울값
    img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    cv2.imshow("HSV", img_cvt)
    hsv_low = (20, 100, 100)
    hsv_high = (40, 255, 255)
    img_mask = cv2.inRange(img_cvt, hsv_low, hsv_high)
    cv2.imshow("MASK", img_mask)
    img_canny = cv2.Canny(img_mask, 200, 200)
    cv2.imshow("CANNY", img_canny)
    rho = 1  # precision in pixel, i.e. 1 pixel
    angle = np.pi / 180  # degree in radian, i.e. 1 degree
    min_threshold = 10  # minimal of votes
    line_segments = cv2.HoughLinesP(img_canny, rho, angle, min_threshold, np.array([]), minLineLength=15, maxLineGap=4)
    point = np.array([ 0, 0, 0, 0])
    
    if line_segments is None :
        pass
    else:
        point = line_segments[0][0]
        print(line_segments[0][0])
    cv2.line(img,(point[0],point[1]),(point[2],point[3]),(0,0,255),5)
   
    cv2.imshow("IMG", img)
    key = cv2.waitKey(1)
    if key&0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
