from sys import argv
from numpy import where, array

def open_file(n):
    """Open and read 'n' cmd argument."""
    with open(argv[n], 'r') as my_file:
        content = my_file.read().split()
    content = [i for i in content]
    return content

def time_to_min(array):
    minutes = []
    for time in array:
        minutes.append(sum(x * int(t) for x, t in zip([60, 1], time.split(":"))))
    return minutes

def in_out(array):
    inn, out = array[::2], array[1::2]
    return inn, out
       

def make_time(array):
    them = []
    for time in array:
        time = str(time//60) + ':' + str(time%60)
        if len(time) < 4:
            time += '0'
            them.append(time)
        else:
            them.append(time)

    return them

mins = time_to_min(open_file(1))
inn, out = in_out(mins)
all_min = [i for i in range(60*24)]
index_list = [0] * 60 * 24
for ind in range(len(inn)):
    for num in all_min:
        if inn[ind] <= num < out[ind]:
            index_list[num] += 1
        else:
            pass

A = array(index_list)
maximum_indices = where(A==max(index_list))
maximum_indices = [item.tolist() for item in maximum_indices]
work = maximum_indices[0]
final = []
for a in range(len(work)):
    if work[a] == work[0]:
        final.append(work[a])
    elif work[a] == work[-1]:
        final.append(work[a] + 1)
    elif work[a] == (work[a-1] + 1) and work[a] != (work[a+1] - 1):
        final.append(work[a] + 1)
    elif work[a] == (work[a+1] - 1) and work[a] != (work[a-1] + 1):
        final.append(work[a])    
one, two = in_out(final)
for num in range(len(one)):
    print(make_time(one)[num] + ' ' + make_time(two)[num])
