import cv2
from arg_parser import init_arg_parser
from filters.blur import blur_manager

parser = init_arg_parser().parse_args()

# Load the image
image = cv2.imread(parser.path)

if image is None:
  raise ValueError('Image not found.')
else:
  # Apply the filters
  blurred_image = blur_manager(image, parser.blur, parser)

  # Save the output image
  if parser.output:
    cv2.imwrite(parser.output, blurred_image)
  else:
    cv2.imwrite('output.jpg', blurred_image)

  