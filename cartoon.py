import cv2
import numpy as np

# Load the image
img = cv2.imread('image2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
gray = cv2.medianBlur(gray, 5)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Convert the image to color
color = cv2.bilateralFilter(img, 9, 300, 300)

# Combine the color image with the edges mask
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Display the cartoon image
# cv2.imshow("cartoon", cartoon)
cartoon_resized = cv2.resize(cartoon, (800, 600))  # 원하는 크기로 조정
cv2.imshow("cartoon", cartoon_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
