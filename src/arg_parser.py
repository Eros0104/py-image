import argparse

def init_arg_parser():
  parser = argparse.ArgumentParser(description='Apply filters to images using OpenCV.')
  parser.add_argument('--path', type=str, required=True, help='Path to the input image.')

  return parser