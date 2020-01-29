from sys import argv
from numpy import percentile, mean

phrases = [
    '90 перцентиль',
    'Медиана',
    'Максимальное значение',
    'Минимальное значение',
    'Среднее значение',
    ]


def open_file(n):
    """Open and read 'n' cmd argument."""
    with open(argv[n], 'r') as my_file:
        content = my_file.read().split()
    content = [float(i) for i in content]
    return content


def calculation(array, quotes=phrases):
    """Create a new list with calculations rounded to hundredths."""
    answer = []
    answer.append(percentile(array, 90))
    answer.append(percentile(array, 50))
    answer.append(max(array))
    answer.append(min(array))
    answer.append(mean(array))
    for num in range(5):
        print(f'{quotes[num]} = {"{0:.2f}".format(answer[num])};')


calculation(open_file(1))
