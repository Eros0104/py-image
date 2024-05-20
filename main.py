import cv2

# Load the image
image = cv2.imread('./example/monkey.png')

if image is None:
  print('Could not open or find the image')
else:
  # Apply Gaussian blur with a kernel size of (15, 15)
  blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

  # Display the original and blurred images
  cv2.imshow('Original Image', image)
  cv2.imshow('Blurred Image', blurred_image)

  # Wait for a key press and close the image windows
  cv2.waitKey(0)
  cv2.destroyAllWindows()