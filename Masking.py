
import cv2 
import numpy as np




image = cv2.imread('motherboard_image.JPEG')
image = cv2.resize(image, (800, 600))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve edge detection
blurred = cv2.GaussianBlur(image,(5, 5), 0)

#Apply adaptive thresholding to create a binary image
#timage = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)

# FIRST ITERATION 
#  edge detection
edges = cv2.Canny(gray ,120, 200)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=12)

if lines is not None:
        # Create a mask for the detected lines
        line_mask = np.zeros_like(edges)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_mask, (x1, y1), (x2, y2), 255, 2)

result2 = cv2.bitwise_and(image, image, mask=line_mask)
kernel = np.ones((38, 38), np.uint8)
line_mask = cv2.morphologyEx(line_mask, cv2.MORPH_CLOSE, kernel)
kernel = np.ones((25, 25), np.uint8)
line_mask = cv2.morphologyEx(line_mask, cv2.MORPH_OPEN, kernel)

result = cv2.bitwise_and(image, image, mask=line_mask)

# SECOND TIME 
edges = cv2.Canny(result ,0, 255)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=15)
if lines is not None:
        # Create a mask for the detected lines
        line_mask = np.zeros_like(edges)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_mask, (x1, y1), (x2, y2), 255, 2)
result1 = cv2.bitwise_and(result, result, mask=line_mask)

kernel = np.ones((100, 100), np.uint8)
line_mask = cv2.morphologyEx(line_mask, cv2.MORPH_CLOSE, kernel)
result = cv2.bitwise_and(image, image, mask=line_mask)

# Display the results
cv2.imshow("Original Image",line_mask)
cv2.imshow(" Image", result)
cv2.imshow("Edges", edges )
cv2.waitKey(1000000000)
cv2.destroyAllWindows()
cv2.waitKey(1)  # Add a small delay (1 millisecond) to allow windows to close







