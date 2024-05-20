import argparse

def init_arg_parser():
  parser = argparse.ArgumentParser(description='Apply filters to images using OpenCV.')
  parser.add_argument('--path', type=str, required=True, help='Path to the input image.')
  # parser.add_argument('--filter', type=str, required=True, choices=['gaussian', 'median', 'bilateral'], help='Filter to apply to the image.')
  # Blur filter arguments
  parser.add_argument('--blur', type=str, choices=['gaussian', 'median'], help='Blur filter to apply to the image.')
  parser.add_argument('--kernel', type=int, help='Kernel size for the filter. For example, pass --kernel 15 for a 15x15 kernel.')
  # Edge detection filter arguments
  parser.add_argument('--edge', type=str, choices=['canny'], help='Edge detection filter to apply to the image.')

  parser.add_argument('--sigma-color', type=float, help='Sigma color for the bilateral filter.')
  parser.add_argument('--sigma-space', type=float, help='Sigma space for the bilateral filter.')
  parser.add_argument('--output', type=str, help='Path to save the output image.')

  return parser