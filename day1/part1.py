# https://adventofcode.com/2022/day/1

from utils import get_calories_for_each_elf, get_input_from_file

def main():
    data = get_input_from_file()
    elfs_calories = get_calories_for_each_elf(data)
    print(max(elfs_calories.values()))

if __name__ == "__main__": main()