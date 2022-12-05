# https://adventofcode.com/2022/day/5

from utils import get_input_from_file
import re

def main():
    stacks = [
        "FHBVRQDP",
        "LDZQWV",
        "HLZQGRPC",
        "RDHFJVB",
        "ZWLC",
        "JRPNTGVM",
        "JRLVMBS",
        "DPJ",
        "DCNWV"
    ]
    data = get_input_from_file()
    for instruction in data:
        stacks = execute_instruction(stacks, instruction)

    for stack in stacks:
        print(stack[-1], end="")

    print()

def execute_instruction(stacks, instruction) -> list:

    numbers = re.findall(r'\d+', instruction)
    numbers = [int(number) for number in numbers]

    for i in range(numbers[0]):
        # get item from source stack
        item = stacks[numbers[1] - 1][-1]
        # add item to destination stack
        stacks[numbers[2] - 1] += item
        # remove item from source stack
        stacks[numbers[1] - 1] = stacks[numbers[1] - 1][:-1]

    return stacks 

if __name__ == '__main__': main()