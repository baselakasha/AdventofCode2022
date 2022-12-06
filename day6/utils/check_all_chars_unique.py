def check_all_chars_unique(string):
    temp = []
    for char in string:
        if char in temp:
            return False
        temp.append(char)
    return True