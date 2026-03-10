import argparse

# description — это текстовое описание программы,
# оно будет показано пользователю при вызове справки (-h или --help)

def main():
  parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')


  parser.add_argument('first_file')
  parser.add_argument('second_file')

  parser.parse_args()