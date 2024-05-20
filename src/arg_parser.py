import argparse

def init_arg_parser():
  parser = argparse.ArgumentParser(description='Apply filters to images using OpenCV.')
  parser.add_argument('--path', type=str, required=True, help='Path to the input image.')
  # parser.add_argument('--filter', type=str, required=True, choices=['gaussian', 'median', 'bilateral'], help='Filter to apply to the image.')
  parser.add_argument('--kernel', type=int, nargs='+', help='Kernel size for the filter. For example, pass --kernel 15 15 for a 15x15 kernel.')
  parser.add_argument('--sigma-color', type=float, help='Sigma color for the bilateral filter.')
  parser.add_argument('--sigma-space', type=float, help='Sigma space for the bilateral filter.')
  parser.add_argument('--output', type=str, help='Path to save the output image.')

  return parser