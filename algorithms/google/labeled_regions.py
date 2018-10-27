# given an array of labeled intervals, with each range to be [start, end)
def get_labeled_regions(intervals):
    if not intervals:
        return []

    events = []
    for start, end, label in intervals:
        events.append((start, label, True))
        events.append((end, label, False))
    events.sort()

    curr_start = -1
    curr_labels = []
    regions = []

    for pos, label, entering in events:
        if not curr_labels:
            curr_start = pos
            curr_labels = [label]
            continue

        region = (curr_start, pos, ''.join(curr_labels))
        regions.append(region)
        curr_start = pos

        if entering:
            curr_labels.append(label)
        else:
            curr_labels.remove(label)

    return regions

def test():
    intervals1 = [(2, 8, 'a'), (3, 5, 'c'), (6, 9, 'b')]
    print get_labeled_regions(intervals1)
    # [(2, 3, 'a'), (3, 5, 'ac'), (5, 6, 'a'), (6, 8, 'ab'), (8, 9, 'b')]

    intervals2 = [(2, 5, 'a'), (3, 7, 'b'), (8, 10, 'c')]
    print get_labeled_regions(intervals2)
    # [(2, 3, 'a'), (3, 5, 'ab'), (5, 7, 'b'), (8, 10, 'c')]


if __name__ == '__main__':
    test()
