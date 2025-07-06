import cv2
import numpy as np
from helpers.centeroids import compute_centroids

for i in range(5, 15):
    img = cv2.imread(f"imgs/{i}.jpeg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(img_gray, 200, 255, 0)

    kernel = np.ones((10, 10), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    cX, cY = compute_centroids(cleaned)

    cv2.circle(img, (cX, cY), 5, (0, 255, 0), -1)

    # text for the centroid
    cv2.putText(img, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Centroid", img)
    cv2.imshow("Thresholded Image", cleaned)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
