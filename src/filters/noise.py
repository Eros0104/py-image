import cv2
import numpy as np

def is_even(number):
  return number % 2 == 0

# Function to apply Gaussian blur to an image
def gaussian_noise(image, params):
  mean = params.mean if params.mean else 0
  stddev = params.stddev if params.stddev else 25

  gaussian = np.random.normal(mean, stddev, image.shape).astype('uint8')
  noisy_image = cv2.add(image, gaussian)
  
  return noisy_image

# Function to apply salt and pepper noise to an image
def salt_and_pepper_noise(image, params):
  salt_prob = params.salt_prob if params.salt_prob else 0.05
  pepper_prob = params.pepper_prob if params.pepper_prob else 0.05

  noisy_image = image.copy()
  total_pixels = image.shape[0] * image.shape[1]
  
  # Sal
  num_salt = int(total_pixels * salt_prob)
  salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
  noisy_image[salt_coords[0], salt_coords[1]] = 255

  # Pimenta
  num_pepper = int(total_pixels * pepper_prob)
  pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
  noisy_image[pepper_coords[0], pepper_coords[1]] = 0
  
  return noisy_image

# Dictionary to map filter types to their respective functions
noise_map = {
  'gaussian': gaussian_noise,
  'salt_pepper': salt_and_pepper_noise,
}

# Function to manage the noise filter
def noise_manager(image, filter_type=None, params=None):
  if filter_type is None:
    return image
  
  if filter_type not in noise_map:
    raise ValueError(f'Filter type {filter_type} not supported. Supported filters are {list(noise_map.keys())}')
  
  return noise_map[filter_type](image, params)
