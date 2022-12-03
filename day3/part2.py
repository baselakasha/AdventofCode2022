# https://adventofcode.com/2022/day/3

import string
from utils import get_input_from_file

def main():
    alpha = string.printable[10:62]
    rucksacks = get_input_from_file()
    total = 0
    for index in range(0, len(rucksacks), 3):
        string1 = rucksacks[index]
        string2 = rucksacks[index+1]
        string3 = rucksacks[index+2]

        common_character = ''.join(set.intersection(set(string1), string2, string3))
        total += alpha.index(common_character) + 1
    
    print(total)

if __name__ == "__main__": main()