import cv2
import numpy as np

img = cv2.imread("./images/bmw-m440i.jpg")
h, w = img.shape[:2] #getting the hight and width of the image (index 0 and 1)... Index 2 goes for depth, which we dont need for this case

img = np.dstack([img, np.ones((h,w), dtype='uint8') * 255])    #create a white "mask" with the same size of the image

logo = cv2.imread("./images/logo.png", cv2.IMREAD_UNCHANGED)

#separing all the layers of the logo image
(B, G, R, A) = cv2.split(logo)
B = cv2.bitwise_and(B, B, mask = A)
G = cv2.bitwise_and(G, G, mask = A)
R = cv2.bitwise_and(R, R, mask = A)
logo = cv2.merge([B, G, R, A])

logo = cv2.resize(logo, (200,200), interpolation = cv2.INTER_AREA)
lH, lW = logo.shape[:2]
bH, bW = h, w
overlay = np.zeros((bH, bW, 4), dtype='uint8')
overlay[bH - lH:bH, bW - lW:bW] = logo

img = cv2.addWeighted(overlay, 0.5, img, 1.0, 0, img)

""" cv2.imshow("logo",logo)
cv2.waitKey(0)
cv2.destroyAllWindows() """

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
