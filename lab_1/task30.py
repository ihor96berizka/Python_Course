import argparse


# define functions for operation with file
def read_file(file_name):
    with open(file_name, 'r') as file:
        reading = file.read()
        return reading


def count_words(file_name):
    file_reading = str(read_file(file_name))
    words = file_reading.split()
    count = len(words)
    print(count)


def count_lines(file_name):
    file_reading = read_file(file_name)
    lines = file_reading.split('/n')
    line_count = len(lines)
    print(line_count)


def count_some_word(file_name, target_word):
    file_reading = read_file(file_name)
    occurrences = file_reading.lower().count(target_word.lower())
    print(occurrences)


# define the main function using argparse module
def main():
    parser = argparse.ArgumentParser(description='Operation with file')
    # subparsers = parser.add_subparsers(dest='operation', help='Available operations')

    # create the parser for the "file" command
    # parser_file = subparsers.add_parser('-f', help="open your file")
    parser.add_argument('-f', '--file', help="Only open your file, you need to use this with '-cw'/'-cl'/'-csw'. Example: -f file_name -cw.")
    parser.add_argument('-cw', '--count_words', action='store_true', help="Count words in your file. Example: -f file_name -cw.")
    parser.add_argument('-cl', '--count_lines', action='store_true', help="Count lines in your file. Example: -f file_name -cl.")
    parser.add_argument('-csw', '--count_some_word', help="Count some word in your file. Example: -f file_name -csw target_word.")

    args = parser.parse_args()

    if args.file:
        if args.count_words:
            count_words(args.file)
        elif args.count_lines:
            count_lines(args.file)
        elif args.count_some_word:
            count_some_word(args.file, args.count_some_word)
        else:
            parser.print_help()


main()
