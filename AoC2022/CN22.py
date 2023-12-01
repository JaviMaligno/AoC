import os
import sys
day = sys.argv[1]
dirname = f"Day{day}"
parent_dir = r"C:\Users\javia\OneDrive\Escritorio\GitHub\AoC2022"
path = os.path.join(parent_dir, dirname)
if not os.path.exists(path):
    os.mkdir(path)
    py_file = os.path.join(path,f"C{day}.py")
    py_test = os.path.join(path,"test.py")
    test_input = os.path.join(path,"test.txt")
    with open(py_file,"a+") as py:
        py.writelines(["import sys\n",
            f'sys.path.append(r"{parent_dir}")\n', 
            "from get_data import get_input\n",
            f"text = get_input({day})\n"])

    with open(py_test, 'a+') as test:
        test.writelines([f"from C{day} import *\n", f'with open(r"{test_input}") as f: pass'])
    open(test_input, 'a').close()






