import os
from abc import ABC, abstractmethod


class FileType(ABC):
    def __init__(self, path, name, is_directory=True):
        self.is_directory = is_directory
        self.path = path
        self.name = name

    @abstractmethod
    def show(self, level = 0):
        pass
    

class SimpleFileType(FileType):

    # def __init__(self, path, name, is_directory=True):
    #     self.is_directory = is_directory
    #     self.path = path
    #     self.name = name

    def show(self, level):
        if level == 0:
            result = f"{self.path}"
        else:
            result = f"{self.name}"

        return result


class FancyFileType(FileType):

    # def __init__(self, path, name, is_directory=True):
    #     self.is_directory = is_directory
    #     self.path = path
    #     self.name = name

    def show(self, level):
        if level == 0:
            result = f"*{self.path}*"
        else:
            result = f"*{self.name}*"

        return result


class DumbFileType(FileType):
    
    def show(self, level):
        return ""


class TypeException(Exception):

    def __init__(self, message, *args: object):
        self.message = message
        super().__init__(*args)

def check_type(value, type_class):
    actual_type = type_class.__name__
    value_class = value.__class__.__name__
    if value_class != actual_type:
        for cls in value.__class__.__bases__:
            if cls.__name__ == actual_type:
                return
        raise TypeException(message=f"Type must be {actual_type}")


class Node:

    def __init__(self, value: FileType = None, is_root = False, children = []):
        
        check_type(value, FileType)
        
        self.value = value
        self.is_root = is_root
        self.children = children
    
    def __str__(self):
        return self.show()

    def show(self, level=0):
        result = self.value.show(level)
        for child in self.children:
            result = result + "\n\r-" + "-"*level + child.show(level + 1)
        return result


def read_directory_structure(root_directory):
    root_files = os.listdir(root_directory)
    value = DumbFileType(path=root_directory, 
        name=root_directory.split(os.sep)[-1])

    root_node = Node(value=value, is_root=True, children=[])
    children = []
    for file in root_files:
        if file[0] != ".":
            child_directory = root_directory + os.sep + file
            if os.path.isdir(child_directory):
                child_node = read_directory_structure(child_directory)
            else:
                child_value = DumbFileType(path=child_directory, 
                    name=child_directory.split(os.sep)[-1])
                child_node = Node(value=child_value, children=[])

            children.append(child_node)
    root_node.children = children

    return root_node


root = read_directory_structure("D:\\src\\py\\python-tutorial")
print(root)




