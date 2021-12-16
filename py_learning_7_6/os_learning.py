from os import listdir
from os.path import isdir, join

file_count = 0


def show_dir(path):
    global file_count
    file_name = 'file_path.txt'
    with open(file_name, 'a') as fp:
        for file in listdir(path):
            temp = join(path, file)
            if isdir(temp):
                try:
                    show_dir(temp)
                except PermissionError:
                    pass
            else:
                file_count += 1
                print(temp)
                temp += '\n'
                fp.write(temp)


work_path = 'C:/Program Files (x86)'
show_dir(work_path)
print("file number：" + str(file_count))

with open('file_path.txt', 'a') as fk:
    fk.write("file number：" + str(file_count))
