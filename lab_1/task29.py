import argparse
import sys

# define the reading file function


def read_file(file_name):
    with open(file_name, 'r') as file:
        output = file.read()
        print(output)

# using sys module


def sys_case():
    x = sys.argv[1]
    return x


# using argparse module


def argparse_case():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="open your file")
    args = parser.parse_args()
    return args.file


def main():
    argparse_arg = argparse_case()
    read_file(argparse_arg)


main()
