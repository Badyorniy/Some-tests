from sys import argv

interval = 0
maximum = 0

def open_file(n):
    """Open and read 'n' file in folder."""
    with open(argv[1] + '\Cash' + str(n) + '.txt', 'r') as my_file:
        content = my_file.read().split()
    content = [float(i) for i in content]
    return content

for n in range(len(open_file(1))):
    a = open_file(1)[n] + open_file(2)[n] + open_file(3)[n] + open_file(4)[n] + open_file(5)[n]
    if  a > maximum:
        maximum = a
        interval = n + 1
print(interval)
    


