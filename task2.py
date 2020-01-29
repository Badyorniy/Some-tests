from sys import argv


def open_file(n):
    """Open and read 'n' cmd argument."""
    with open(argv[n], 'r') as my_file:
        content = my_file.read().split()
    content = [float(i) for i in content]
    return content


def check(first_list, second_list):
    """Check dot position in polygon."""
    quad_x, quad_y = first_list[::2], first_list[1::2]
    dots_x, dots_y = second_list[::2], second_list[1::2]
    for i in range(len(dots_x)):
        if (dots_x[i] > max(quad_x) or dots_x[i] < min(quad_x)) or (dots_y[i] > max(quad_y) or dots_y[i] < min(quad_y)):
            print(3) # точка снаружи
        elif (max(quad_x) > dots_x[i] > min(quad_x)) and (max(quad_y) > dots_y[i] > min(quad_y)):
            print(2) # точка внутри
        elif (dots_y[i] == min(quad_y) or max(quad_y)) and (min(quad_x) < dots_x[i] < max(quad_x)):
            print(1) # точка на одной из сторон
        elif (dots_x[i] == min(quad_x) or max(quad_x)) and (min(quad_y) < dots_y[i] < max(quad_y)):
            print(1) # точка на одной из сторон
        else:
            for num in range(len(quad_x)):
                if (quad_x[num] == dots_x[i]) and (quad_y[num] == dots_y[i]):
                     print(0) # точка на одной из вершин

quad = open_file(1)
dots = open_file(2)           
check(quad, dots)

