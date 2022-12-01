def get_input_from_file():
    with open("input.txt", "r") as file_:
        return [d[0: len(d) -1] for d in file_.readlines()]