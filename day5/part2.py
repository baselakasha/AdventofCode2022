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

    # get items from source stack
    items = stacks[numbers[1] - 1][-numbers[0]:]
    # add items to destination stack
    stacks[numbers[2] - 1] += items
    # remove items from source stack
    stacks[numbers[1] - 1] = stacks[numbers[1] - 1][:-numbers[0]]

    return stacks 

if __name__ == '__main__': main()