import cv2
import numpy as np
from helpers.centeroids import compute_centroids

def distance_from_center(img_path):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(img_gray, 200, 255, 0)

    kernel = np.ones((10, 10), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    cX, cY = compute_centroids(cleaned)

    cv2.circle(img, (cX, cY), 5, (0, 255, 0), -1)

    # Save the modified image with the center marked
    output_path = img_path.replace('.jpg', '_centered.jpg').replace('.jpeg', '_centered.jpeg')
    cv2.imwrite(output_path, img)

    _, width = img.shape[:2]
    center_x = width // 2

    # Distance in pixels
    distance = cX - center_x
    return distance
