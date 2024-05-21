import cv2
import numpy as np

def ideal_low_pass_filter(image):
  # Convert image to grayscale if it's not already
  if len(image.shape) == 3:
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  else:
      gray = image

  # Compute 2D Fourier Transform
  f = np.fft.fft2(gray)
  fshift = np.fft.fftshift(f)

  # Define mask for ideal low-pass filter
  rows, cols = gray.shape
  crow, ccol = rows // 2, cols // 2
  mask = np.zeros((rows, cols), np.uint8)
  mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

  # Apply mask to the Fourier transformed image
  fshift = fshift * mask

  # Inverse Fourier Transform
  f_ishift = np.fft.ifftshift(fshift)
  img_back = np.fft.ifft2(f_ishift)
  img_back = np.abs(img_back)

  return img_back.astype(np.uint8)

def ideal_high_pass_filter(image):
  # Convert image to grayscale if it's not already
  if len(image.shape) == 3:
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  else:
      gray = image

  # Compute 2D Fourier Transform
  f = np.fft.fft2(gray)
  fshift = np.fft.fftshift(f)

  # Define mask for ideal high-pass filter
  rows, cols = gray.shape
  crow, ccol = rows // 2, cols // 2
  mask = np.ones((rows, cols), np.uint8)
  mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0

  # Apply mask to the Fourier transformed image
  fshift = fshift * mask

  # Inverse Fourier Transform
  f_ishift = np.fft.ifftshift(fshift)
  img_back = np.fft.ifft2(f_ishift)
  img_back = np.abs(img_back)

  return img_back.astype(np.uint8)

# Dictionary to map filter types to their respective functions
fourier_map = {
  'low': ideal_low_pass_filter,
  'high': ideal_high_pass_filter,
}

# Function to manage the fourier filter
def fourier_transform_manager(image, filter_type = None):
  if filter_type is None:
    return image
  
  if filter_type not in fourier_map:
    raise ValueError(f'Filter type {filter_type} not supported. Supported filters are {list(fourier_map.keys())}')

  return fourier_map[filter_type](image)