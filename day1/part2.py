# https://adventofcode.com/2022/day/1#part2

from utils import get_calories_for_each_elf, get_input_from_file

def main():
    data = get_input_from_file()
    elfs_calories = get_calories_for_each_elf(data)
    
    # get top 3 elves
    sorted_values = sorted((elfs_calories).values(), reverse=True)
    print(sorted_values[0] + sorted_values[1] + sorted_values[2])

if __name__ == "__main__": main()