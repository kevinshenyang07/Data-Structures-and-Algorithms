# give an array of sorted and non-overlapping intervals, insert a number
# if the number is next to the start or end of an interval, merge nearby intervals
# otherwise insert [num, num] into the intervals
def insert(intervals, num):
    # insert [num, num] into intervals
    insert_idx = -1
    for i, interval in enumerate(intervals):
        if num < interval[0]:
            insert_idx = i
            break
    intervals.insert(insert_idx, [num, num])

    res = []

    for interval in intervals:
        if not res:
            res.append(interval)
        else:
            prev = res[-1]
            if abs(prev[1] - interval[0]) <= 1:
                res[-1] = [prev[0], interval[1]]
            else:
                res.append(interval)

    return res

def test():
    print insert([[1,2], [4,5], [9,10]], 7)  # [[1,2], [4,5], [7,7], [9,10]]
    print insert([[1,2], [4,5], [9,10]], 3)  # [[1,5], [9,10]]


if __name__ == '__main__':
    test()
