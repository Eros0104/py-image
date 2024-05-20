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

def band_pass_filter(image, low_cutoff = 5, high_cutoff = 30):
  # Convert image to grayscale if it's not already
  if len(image.shape) == 3:
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  else:
      gray = image

  # Compute 2D Fourier Transform
  f = np.fft.fft2(gray)
  fshift = np.fft.fftshift(f)

  # Get dimensions of the image
  rows, cols = gray.shape
  crow, ccol = rows // 2, cols // 2

  # Create ideal high-pass filter
  high_pass_mask = np.ones((rows, cols), np.uint8)
  high_pass_mask[crow - high_cutoff:crow + high_cutoff, ccol - high_cutoff:ccol + high_cutoff] = 0

  # Create ideal low-pass filter
  low_pass_mask = np.zeros((rows, cols), np.uint8)
  low_pass_mask[crow - low_cutoff:crow + low_cutoff, ccol - low_cutoff:ccol + low_cutoff] = 1

  # Combine the high-pass and low-pass masks to create band-pass filter
  band_pass_mask = high_pass_mask * low_pass_mask

  # Apply mask to the Fourier transformed image
  fshift = fshift * band_pass_mask

  # Inverse Fourier Transform
  f_ishift = np.fft.ifftshift(fshift)
  img_back = np.fft.ifft2(f_ishift)
  img_back = np.abs(img_back)

  return img_back.astype(np.uint8)

# Dictionary to map filter types to their respective functions
fourierMap = {
  'low': ideal_low_pass_filter,
  'high': ideal_high_pass_filter,
  'band': band_pass_filter
}

# Function to manage the fourier filter
def fourier_transform_manager(image, filter_type = None):
  if filter_type is None:
    return image
  
  if filter_type not in fourierMap:
    raise ValueError(f'Filter type {filter_type} not supported. Supported filters are {list(fourierMap.keys())}')

  return fourierMap[filter_type](image)