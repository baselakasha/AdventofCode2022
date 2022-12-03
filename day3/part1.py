# https://adventofcode.com/2022/day/3

import string
from utils import get_input_from_file

def main():
    alpha = string.printable[10:62]
    rucksacks = get_input_from_file()
    total = 0
    for rucksack in rucksacks:
        length = len(rucksack)
        half_index = int(length/2)

        half1 = rucksack[0:half_index]
        half2 = rucksack[half_index:length]

        common_character = ''.join(
            set(half1).intersection(half2)
        )

        total += alpha.index(common_character) + 1

    print(total)

if __name__ == "__main__": main()