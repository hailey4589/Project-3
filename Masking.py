
import cv2 
import numpy




image = cv2.imread('motherboard_image.JPEG')
cv2.imshow("1", image)
cv2.waitKey(100000)
cv2.destroyAllWindows()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve edge detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to create a binary image
thresholded = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)

# Apply Canny edge detection
edges = cv2.Canny(image, 30, 150)

# Find contours in the edged image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area (adjust the area threshold accordingly)
min_contour_area = 1000
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]

# Draw contours on the original image
cv2.drawContours(image, filtered_contours, -1, (0, 255, 0), 2)

# Display the results
#cv2.imshow("Original Image", image)
cv2.imshow("Thresholded Image", thresholded)
#cv2.imshow("Edges", edges)
cv2.waitKey(1000000000)
cv2.destroyAllWindows()

