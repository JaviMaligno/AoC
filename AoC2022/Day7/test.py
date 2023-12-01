from C7 import Dir, directories, small_dirs, free_up_space

with open(r"Day7\test.txt") as f:
    text = f.read().splitlines()
    """ print(directories(text, Dir).directories['a'].directories['e'].directories)
    print(directories(text, Dir).directories['a'].directories['e'].files) """
    # parents were copies pointing to different memory addresses
    """ print(directories(text, Dir).directories['a'].parent.set_size(3))
    print(directories(text, Dir).directories['d'].parent._size) """
    root = directories(text, Dir)
    #print([root.directories[a].files_size() for a in root.directories])
    subdirs = root.directories
    #print(sum(small_dirs(subdir) for subdir in subdirs.values()))
    print(small_dirs(root))
    print(free_up_space(root))