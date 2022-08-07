import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
	ret, img = cap.read() # img image ret:return value
	img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	cv2.imshow("BGR", img)
	cv2.imshow("HSV", img_cvt)
	hsv_low = (10, 100, 100)
	hsv_high = (50, 255, 255)
	img_mask = cv2.inRange(img_cvt, hsv_low, hsv_high)
	cv2.imshow("Mask", img_mask);
	img_canny = cv2.Canny(img_mask, 100, 900)
	cv2.imshow("CANNY", img_canny)
	key = cv2.waitKey(1)
	if key&0xff == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
