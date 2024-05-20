import cv2
from arg_parser import init_arg_parser

parser = init_arg_parser().parse_args()

# Load the image
image = cv2.imread(parser.path)

if image is None:
  print('Could not open or find the image')
else:
  # Apply Gaussian blur with a kernel size of (15, 15)
  blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

  # Save the output image
  if parser.output:
    cv2.imwrite(parser.output, blurred_image)
  else:
    cv2.imwrite('output.jpg', blurred_image)

  