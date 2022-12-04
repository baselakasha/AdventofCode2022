# https://adventofcode.com/2022/day/4

from utils import get_input_from_file

def main():
    data = get_input_from_file()
    number_of_pairs_that_overlap = 0
    for line in data:
        pairs = line.split(",")
        first_pair_range = pairs[0].split("-")
        second_pair_range = pairs[1].split("-")

        if do_ranges_overlap(first_pair_range, second_pair_range):
            number_of_pairs_that_overlap +=1
    
    print(number_of_pairs_that_overlap)

def do_ranges_overlap(range1, range2):
    range1_range = range(int(range1[0]), int(range1[1]) + 1)
    range2_range = range(int(range2[0]), int(range2[1]) + 1)

    return any(x in range1_range for x in range2_range)

if __name__ == '__main__': main()
