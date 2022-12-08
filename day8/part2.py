# https://adventofcode.com/2022/day/8

from utils import get_input_from_file

def main():
    grid = get_input_from_file()
    trees_scores = []
    for row_index, row in enumerate(grid):
        for tree_index, tree, in enumerate(row):
            # check if its on the top or left edge
            if row_index == 0 or tree_index == 0:
                trees_scores.append(0)
                continue
            
            # check if its on the bottom or right edge
            if row_index == len(grid)-1 or tree_index == len(row) - 1:
                trees_scores.append(0)
                continue

            tree_scores = []


            top_trees = get_top_trees(grid, row_index, tree_index)
            tree_scores.append(get_view_distance(tree, top_trees[::-1]))
    

            left_trees = row[:tree_index]
            tree_scores.append(get_view_distance(tree, left_trees[::-1]))
            
        
            right_trees = row[tree_index+1:]
            tree_scores.append(get_view_distance(tree, right_trees))


            bottom_trees = get_bottom_trees(grid, row_index, tree_index)
            tree_scores.append(get_view_distance(tree, bottom_trees))

            tree_score = 1
            for score in tree_scores:
                tree_score = tree_score * score

            # debugging 
            # print(tree_index, tree, tree_scores, tree_score)
            # print("____________")
        
            trees_scores.append(tree_score)

    print(
        sorted([x for x in list(set(trees_scores)) if x != 0])
    )


def get_view_distance(tree, view_trees):
    for view_tree_index, view_tree in enumerate(view_trees):
        if view_tree >= tree:
            break
    return view_tree_index + 1

def get_top_trees(grid, row_index, tree_index):
    trees_top = ""
    for row_ in grid[:row_index]:
        trees_top += row_[tree_index]
    return trees_top


def get_bottom_trees(grid, row_index, tree_index):
    trees_bottom = ""
    for row_in in grid[row_index+1:]:
        trees_bottom += row_in[tree_index]
    return trees_bottom
    
if __name__ == "__main__": main()