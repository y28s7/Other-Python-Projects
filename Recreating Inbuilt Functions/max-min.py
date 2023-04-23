def nmax(iterable: list):
    highest_number = 0
    for num in iterable:
        if num >= highest_number:
            highest_number = num
    return highest_number


def nmin(iterable: list):
    lowest_number = 0
    for num in iterable:
        if num <= lowest_number:
            lowest_number = num
    return lowest_number
