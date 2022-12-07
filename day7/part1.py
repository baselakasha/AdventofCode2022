from utils import get_input_from_file
from file_system import FileSystem, parse_command_lines

def main():
    filesystem = FileSystem()
    data = get_input_from_file()
    filesystem = parse_command_lines(filesystem, data)
    filesystem.print_structure()

    folders = filesystem.get_folders_with_size()
    the_sum = 0
    for folder in folders:
        if folder["size"] < 100000:
            the_sum += folder["size"]
    print(the_sum)


if __name__ == "__main__": main()