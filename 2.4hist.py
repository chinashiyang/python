def distribute(histogram, x):
    lst = [0] * x
    minimum = min(histogram)
    maximum = max(histogram)
    interval = (maximum - minimum) / x
    for i in histogram:
        index = int((i - minimum) / interval)
        if (i - minimum) != 0 and (i - minimum) % interval == 0:
            index -= 1
        lst[int(index)] += 1
    return lst


assert distribute([1.25, 1, 2, 1.75], 2) == [2, 2]
