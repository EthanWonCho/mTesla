import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
	ret, img = cap.read()
	img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	hsv_low = (0, 100, 100)
	hsv_high = (40, 255, 255)
	img_mask1 = cv2.inRange(img_cvt, hsv_low, hsv_high)
	
	hsv_low = (160, 100, 100)
	hsv_high = (180, 255, 255)
	img_mask2 = cv2.inRange(img_cvt, hsv_low, hsv_high)
	img_canny = cv2.Canny(img_mask1+img_mask2, 200, 200)
	cv2.imshow("CANNY", img_canny)
	'''
	#show lines
	rho = 1
	angle = np.pi
	min_threshold = 10
	
	line_segments = cv2.HoughLinesP(img_canny, rho, angle, min_threshold, np.array([]), minLineLength=15, maxLineGap=4)
	point = np.array([ 0, 0, 0, 0])

	if line_segments is None :
		pass
	else:
		point = line_segments[0][0]
		print(line_segments[0][0])
	cv2.line(img, (point[0],point[1]),(point[2],point[3]),(0,0,255),5)
	'''
	'''
	img_con, contours, hierarchy = cv2.findContours(img_mask2, 1, cv2.CHAIN_APPROX_NONE)
	if len(contours) > 0:
		c = max(contours, key = cv2.contourArea)
		cv2.drawContours(img, c, -1, (0,255,0), 1)
	#cv2.imshow("Mask", img_mask1 + img_mask2)
	'''
	img, contours, hierachy = cv2.findContours(img_canny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	c = max(contours, key=cv2.contourArea)
	cx = 0
	cy = 0
	try:
		M = cv2.moments(c)
		img = cv2.drawContours(image, c, -1, (0,255,0), 3)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
	
		print(cx, cy)
		image = cv2.circle(image, (cx,cy), 10, (0,0,255), -1)
		cv2.imshow('image', image)
		
	except:
		pass
	key = cv2.waitKey(1)
	if key&0xff == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()
