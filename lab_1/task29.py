import argparse
import sys

# using sys module

x = sys.argv[1]


def main(file):
    with open(file, 'r') as f:
        output = f.read()
        print(output)


main(x)

# using argparse module

parser = argparse.ArgumentParser()

parser.add_argument('file')

args = parser.parse_args()

main(args.file)
