s = "This is a learning for 'read() and readline()'.\nThis is second line.\n"
with open('file_learning.txt', 'w') as file_learning:
    file_learning.write(s)

with open('file_learning.txt', 'r') as file_learning:
    an_line = file_learning.readline()
    print(file_learning.tell())

with open('file_learning.txt', 'r') as file_learning:
    lines = file_learning.readlines()

for line in lines:
    print(line)

print(an_line)
