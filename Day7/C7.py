import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
from singleton_decorator import singleton

text = get_input(7).splitlines()
print(text[1:10])

# for the next one create a makefile or something that creates the directorry and files and fills the above

@singleton
class Dir:
    def __init__(self, dir_name, parent = None, size = 0) -> None:
        self.name = dir_name
        self.files = {}
        self.directories = {}
        self._parent = parent
        self._size = size
    
    def add_file(self, file_name, size):
        self.files[file_name] = size

    def add_dir(self, dir_name):
        self.directories[dir_name] = Dir(dir_name)

    @property
    def parent(self):
        return self._parent
   
    @property.setter
    def add_parent(self, parent_dir):
        self._parent = parent_dir

    @property
    def size(self):
        return self._size
    
    @property.setter
    def compute_size(self):
        #loop throught files adding the filesizes and then through subdirectories
        # I will need to think how to really access subdirectories, maybe I will simplify this and just  throw everything into a list
        pass

root = Dir('/')
current_dir = root
for command in text[1:]:
    split = command.split(' ')
    if split[1] == "cd":
        if split[2] == "..":
            current_dir = current_dir.parent
            continue
        elif split[2] == "/":
            current_dir = root
        else:
            current_dir = Dir(split[2], parent = current_dir)
    elif split[1] == "ls":
        continue
    else: 
        if split[0] == "dir":
            subdir = Dir(split[1], parent = current_dir)
            current_dir.add_dir(subdir)
        else:
            current_dir.add_file(split[1], int(split[0]))

        





        

    