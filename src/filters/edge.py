import cv2

# Function to apply Canny edge detection to an image
def canny_edge_detection(image):
  return cv2.Canny(image, 50, 200)

# Dictionary to map filter types to their respective functions
edge_map = {
  'canny': canny_edge_detection
}

# Function to manage the edge detection filter
def edge_detection_manager(image, filter_type = None):
  if filter_type is None:
    return image
  
  if filter_type not in edge_map:
    raise ValueError(f'Filter type {filter_type} not supported. Supported filters are {list(edge_map.keys())}')

  return edge_map[filter_type](image)