import cv2
from helpers.centeroids import compute_centroids

img = cv2.imread("imgs/7.jpeg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img_gray, 180, 255, 0)
cX, cY = compute_centroids(thresh)

cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)

# text for the centroid
cv2.putText(img, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("Centroid", img)
cv2.imshow("Thresholded Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()