class Object:
    def __init__(self, name, path) ->None:
        self.name = name
        self.path = path

class File(Object):
    def __init__(self, size, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.size = size

class Folder(Object):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.children = []

class Storage:
    _tree = [
        Folder(
            name="root",
            path="/"
        )
    ]

    def add_object(self, type, path, size=None):
        path_split = path.split("/")[1:]
        if path_split[-1] == "":
            path_split = path_split[0:-1]

        object_name = path_split[len(path_split) - 1]

        parent_folder = self._get_parent_folder_of_path(path_split)
        if not self._does_object_exist(parent_folder, object_name):
            if size:
                parent_folder.children.append(type(
                    name=object_name,
                    path=path,
                    size=size
                ))
            else:
                parent_folder.children.append(type(
                    name=object_name,
                    path=path
                ))

    def get_root(self):
        return self._tree[0]
            
    def _get_parent_folder_of_path(self, path_split:list):
        parent_path = path_split[0:-1]
        parent_folder = self.get_root()
        for fa in parent_path:
            for child in parent_folder.children:
                if isinstance(child, File):
                    continue
        
                if child.name == fa:
                    parent_folder = child
                    break
        return parent_folder

    def _does_object_exist(self, parent_folder, name):
        for child in parent_folder.children:
            if child.name == name:
                return True
        return False

class FileSystem:
    _storage = Storage()

    def add_folder(self, path:str) -> None:
        if path == "/":
            return

        self._storage.add_object(
            Folder,
            path=path
        )

    def add_file(self, size:int, path:str) -> None:
        self._storage.add_object(
            File,
            path=path,
            size=size
        )

    def print_structure(self):
        def print_tree(folder, depth=0):
            print( " "*depth + "|_" + folder.name)
            for child in folder.children:
                if isinstance(child, File):
                    print(" "*(depth+1) + "|_" + child.name + " (file)" + " ("+str(child.size)+")")
                    continue
                print_tree(child, depth+1)

        print_tree(self._storage.get_root())
    
    def get_folders_with_size(self):
        folders = []

        def get_folder_size(folder):
            size = 0
            for child in folder.children:
                if isinstance(child, File):
                    size += child.size
                    continue

                size += get_folder_size(child)
            
            return size

        def get_folders(folder, depth=0):
            folders.append({
                "name": folder.name,
                "size": get_folder_size(folder)
            })

            for child in folder.children:
                if isinstance(child, File):
                    continue

                get_folders(child, depth+1)

        get_folders(self._storage.get_root())
        return folders

def parse_command_lines(filesystem, data):
    current_path = None
    for line in data:
        if line.startswith("$"):
            if line.startswith("$ cd"):
                folder_path = line.split("$ cd ")[1]
                if folder_path == "..":
                    current_path = current_path.split("/")[0:-2]
                    current_path = "/".join(current_path) + "/"
                    if not current_path:
                        current_path = "/"
                else:
                    if not current_path:
                        current_path = folder_path
                    else:
                        current_path += folder_path + "/"
                        filesystem.add_folder(current_path)
            elif line.startswith("$ ls"):
                continue
        
        elif line.startswith("dir"):
            filesystem.add_folder(current_path + "/" + line.split("dir ")[1] + "/")

        else:
            split = line.split(" ")
            filesystem.add_file(int(split[0]), current_path + split[1])

    return filesystem
