import argparse

def init_arg_parser():
  parser = argparse.ArgumentParser(description='Apply filters to images using OpenCV.')
  parser.add_argument('--path', type=str, required=True, help='Path to the input image.')

  # Blur filter arguments
  parser.add_argument('--blur', type=str, choices=['gaussian', 'median'], help='Blur filter to apply to the image.')
  parser.add_argument('--kernel', type=int, help='Kernel size for the filter. For example, pass --kernel 15 for a 15x15 kernel.')
  parser.add_argument('--sigma', type=float, help='Sigma value for the Gaussian blur filter.')

  # Edge detection filter arguments
  parser.add_argument('--edge', type=str, choices=['canny'], help='Edge detection filter to apply to the image.')

  # Fourier Transform filter arguments
  parser.add_argument('--fourier', type=str, choices=['low', 'high'], help='Fourier Transform filter to apply to the image.')

  # Noise filter arguments
  parser.add_argument('--noise', type=str, choices=['gaussian', 'salt_pepper'], help='Noise filter to apply to the image.')
  parser.add_argument('--mean', type=int, help='Mean value for the Gaussian noise filter.')
  parser.add_argument('--stddev', type=int, help='Standard deviation value for the Gaussian noise filter.')
  parser.add_argument('--salt_prob', type=float, help='Probability of salt noise for the salt and pepper noise filter.')
  parser.add_argument('--pepper_prob', type=float, help='Probability of pepper noise for the salt and pepper noise filter.')

  # Output image path
  parser.add_argument('--output', type=str, help='Path to save the output image.')

  return parser