def get_input_from_file():
    with open("input.txt", "r") as file_:
        return [d.strip() for d in file_.readlines()]