import cv2

def is_even(number):
  return number % 2 == 0

# Function to apply Gaussian blur to an image
def gaussian_blur(image, params):
  kernel_size = params.kernel if params.kernel else 51
  sigma = params.sigma if params.sigma else 0

  if is_even(kernel_size):
    kernel_size += 1

  return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

# Function to apply median blur to an image
def median_blur(image, params):
  kernel_size = params.kernel if params.kernel else 51

  if is_even(kernel_size):
    kernel_size += 1

  return cv2.medianBlur(image, kernel_size)

# Dictionary to map filter types to their respective functions
blur_map = {
  'gaussian': gaussian_blur,
  'median': median_blur
}

# Function to manage the blur filter
def blur_manager(image, filter_type = None, params = None):
  if filter_type is None:
    return image
  
  if filter_type not in blur_map:
    raise ValueError(f'Filter type {filter_type} not supported. Supported filters are {list(blur_map.keys())}')

  return blur_map[filter_type](image, params)