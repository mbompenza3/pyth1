import os
import os.path
import shutil

# shutil.copytree("tests", "tests/tests")
#
for current_dir, dirs, files in os.walk("."):
    # print(current_dir, dirs, files)
    for d in dirs:
        for f in files:
            if f.endswith('.py'):
                print(f)
                print(d)
                print(current_dir)
                break
# print(os.getcwd())
# print(os.listdir("tests"))
# print(os.path.exists('files.py'))
# print(os.path.exists('files1.py'))
# print(os.path.isfile('files.py'))
# print(os.path.isdir('files.py'))
# os.chdir()