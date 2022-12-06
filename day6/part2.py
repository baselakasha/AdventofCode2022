# https://adventofcode.com/2022/day/6

from utils import get_input_from_file, get_index_of_first_unique_chars_of_length

def main():
    data = get_input_from_file()
    print(get_index_of_first_unique_chars_of_length(data[0], 14))

if __name__ == '__main__': main()
