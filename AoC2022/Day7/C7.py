import sys
sys.path.append(r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022")
from get_data import get_input
#from singleton_decorator import singleton

text = get_input(7).splitlines()

# for the next one create a makefile or something that creates the directorry and files and fills the above

#@singleton
class Dir:
    def __init__(self, dir_name, parent = None, size = 0) -> None:
        self.name = dir_name
        self.files = {}
        self.directories = {}
        self.parent = parent
        self._size = size
    
    def add_file(self, file_name, size):
        self.files[file_name] = size

    def add_dir(self, dir):
        self.directories[dir.name] = dir

    """ @property
    def parent(self):
        return self._parent
   
    @property.setter
    def add_parent(self, parent_dir):
        self._parent = parent_dir """
    
    #@property
    def size(self):
        return self._size
    
    #@size.setter #this is used to compute, not to set, redefine
    def set_size(self, size, increment = False, compute = False):
        if compute:
            self._size = self.compute_size()
        elif increment:
            self._size += size
        else:
            self._size = size



    def compute_size(self):
        #loop throught files adding the filesizes and then through subdirectories
        # I will need to think how to really access subdirectories, maybe I will simplify this and just  throw everything into a list
        return self.files_size() + sum(subdir.compute_size() for subdir in self.directories.values())
    
    def files_size(self):
        return sum(size for file, size in self.files.items())
            

def directories(text, Dir):
    root = Dir('/')
    current_dir = root
    for command in text[1:]:
        split = command.split(' ')
        if split[1] == "cd":
            if split[2] == "..":
                current_dir = current_dir.parent if current_dir != root else root
            elif split[2] == "/":
                current_dir = root
            else:
                current_dir = current_dir.directories[split[2]]
        elif split[1] == "ls":
            continue
        else: 
            if split[0] == "dir":
                subdir = Dir(split[1], parent = current_dir) #assigning the parent seems to create a differet copy so the parent is not going to be used
                current_dir.add_dir(subdir)
            else:
                current_dir.add_file(split[1], int(split[0]))
    return root

root = directories(text, Dir)

#print(root)

#print(root.directories['nns'].directories['gjhp'].directories)
            
         
def small_dirs(root, limit_size = 100000):
    small_size = 0
    # files_size = root.files_size()
    subdirs = root.directories
    # small_size += sum(small_dirs(subdir) for subdir in subdirs.values())
    total_size = root.compute_size()
    subdirs_sizes = sum(small_dirs(subdir) for subdir in subdirs.values() )
    small_size += total_size + subdirs_sizes if total_size <= limit_size else subdirs_sizes
    return small_size
    # return small_size+files_size if small_size+files_size <= limit_size else small_size

total_space = 70000000
necessary_space = 30000000
total_size = root.compute_size()
free_space = total_space - total_size
need = necessary_space - free_space


def free_up_space(root, best = total_size):
    subdirs = root.directories.values()
    if free_space > necessary_space:
        return 0
    else:       
        return min([best_choice(root)]+[free_up_space(subdir) for subdir in subdirs])
        

def best_choice(root, best = total_size):    
    if free_space > necessary_space:
        return 0
    subdirs = root.directories.values()
    for subdir in subdirs:
        subdir_size = subdir.compute_size()
        if need <=  subdir_size <= best:
            best = subdir_size

    return best #min(best, *[best_choice(subdir, best) for subdir in subdirs])

print(small_dirs(root))
print(free_up_space(root))


       


        

    
