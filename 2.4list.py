def dist(data, k):
    lst = [0] * k
    minimum = min(data)
    maximum = max(data)
    interval = (maximum - minimum) / k
    for i in data:
        index = int((i - minimum) / interval)
        if (i - minimum) != 0 and (i - minimum) % interval == 0:
            index -= 1
        lst[int(index)] += 1
    return lst


assert dist([1.25, 1, 2, 1.75], 2) == [2, 2]