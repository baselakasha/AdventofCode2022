from utils import get_input_from_file
from file_system import FileSystem, parse_command_lines

def main():
    filesystem = FileSystem()
    data = get_input_from_file()
    filesystem = parse_command_lines(filesystem, data)
    filesystem.print_structure()

    folders = filesystem.get_folders_with_size()
    required_by_update = 30000000
    disks_space = 70000000
    used_space = folders[0]["size"]
    unused_space = disks_space-used_space
    folders.sort(key=lambda x: x["size"], reverse=False)
    for folder in folders:
        if folder["size"] + unused_space > required_by_update:
            break
    print(folder["size"])


if __name__ == "__main__": main()