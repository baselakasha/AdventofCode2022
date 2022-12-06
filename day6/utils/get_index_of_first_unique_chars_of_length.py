from . import check_all_chars_unique

def get_index_of_first_unique_chars_of_length(string, length):
    length = length -1
    chars_count = 0
    for i in range(len(string)):
        if i < length:
            continue

        last_n_chars = string[i-length: i+1]
        if check_all_chars_unique(last_n_chars):
            chars_count = i + 1
            break

    return chars_count
