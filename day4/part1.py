# https://adventofcode.com/2022/day/4

from utils import get_input_from_file

def main():
    data = get_input_from_file()
    number_of_pairs_contain_each_other = 0
    for line in data:
        pairs = line.split(",")
        first_pair_range = pairs[0].split("-")
        second_pair_range = pairs[1].split("-")

        if do_ranges_contain_each_other(first_pair_range, second_pair_range):
            number_of_pairs_contain_each_other += 1
    
    print(number_of_pairs_contain_each_other)

def do_ranges_contain_each_other(range1, range2):
    range1 = [int(range1[0]), int(range1[1])]
    range2 = [int(range2[0]), int(range2[1])]

    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        return True

    if range2[0] <= range1[0] and range2[1] >= range1[1]:
        return True

    return False


if __name__ == '__main__': main()