# https://adventofcode.com/2022/day/8

from utils import get_input_from_file

def main():
    grid = get_input_from_file()
    trees_that_are_visible = get_number_of_trees_the_are_visible(grid)
    print(trees_that_are_visible)

def get_number_of_trees_the_are_visible(grid):
    trees_that_are_visible = 0
    for row_index, row in enumerate(grid):
        for tree_index, tree, in enumerate(row):
            tree = int(tree)
            if check_if_tree_is_visible(tree, row_index, tree_index, grid, row):
                trees_that_are_visible += 1
    return trees_that_are_visible

def check_if_tree_is_visible(tree, row_index, tree_index, grid, row):
    # check if its on the top or left edge
    if row_index == 0 or tree_index == 0:
        return True
    
    # check if its on the bottom or right edge
    if row_index == len(grid)-1 or tree_index == len(row) - 1:
        return True

    trees_to_the_right = row[tree_index+1:]
    if check_if_all_element_are_less_than_item(tree, trees_to_the_right):
        return True
    
    trees_to_the_left = row[:tree_index]
    if check_if_all_element_are_less_than_item(tree, trees_to_the_left):
        return True

    trees_top = get_top_trees(grid, row_index, tree_index)
    if check_if_all_element_are_less_than_item(tree, trees_top):
        return True

    trees_bottom = get_bottom_trees(grid, row_index, tree_index)
    if check_if_all_element_are_less_than_item(tree, trees_bottom):
        return True

def get_bottom_trees(grid, row_index, tree_index):
    trees_bottom = ""
    for row_in in grid[row_index+1:]:
        trees_bottom += row_in[tree_index]
    return trees_bottom

def get_top_trees(grid, row_index, tree_index):
    trees_top = ""
    for row_ in grid[:row_index]:
        trees_top += row_[tree_index]
    return trees_top

def check_if_all_element_are_less_than_item(item, items):
    return all([int(item_to_compare) < item for item_to_compare in items])

            
if __name__ == "__main__": main()