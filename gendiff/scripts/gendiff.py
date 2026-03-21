import argparse
import json
from ..diff import generate_diff


def main():
  parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')


  parser.add_argument('first_file')
  parser.add_argument('second_file')
  parser.add_argument('-f', '--format', dest='format', metavar='FORMAT', help='set format of output')

  args = parser.parse_args()

  with open(args.first_file) as f:
    data1 = json.load(f)
  with open(args.second_file) as f:
    data2 = json.load(f)
  
  result = generate_diff(data1, data2)

  return result
