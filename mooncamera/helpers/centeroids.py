import cv2

def compute_centroids(image):
    """
    Compute the centroids of the white pixels in a grayscale image.
    
    Args:
        image (numpy.ndarray): Grayscale image.
        
    Returns:
        tuple: Coordinates of the centroid (cX, cY).
    """
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    M = cv2.moments(thresh)
    
    if M["m00"] == 0:
        return None
    
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    return cX, cY
