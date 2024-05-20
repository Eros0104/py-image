import cv2
from arg_parser import init_arg_parser
from filters.blur import blur_manager
from filters.edge import edge_detection_manager
from filters.fourier import fourier_transform_manager

parser = init_arg_parser().parse_args()

# Load the image
image = cv2.imread(parser.path)

if image is None:
  raise ValueError('Image not found.')
else:
  # Apply the filters
  image = blur_manager(image, parser.blur, parser)
  image = edge_detection_manager(image, parser.edge)
  image = fourier_transform_manager(image, parser.fourier)

  # Save the output image
  if parser.output:
    cv2.imwrite(parser.output, image)
  else:
    cv2.imwrite('output.jpg', image)

  