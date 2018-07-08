from heapq import heappush, heappop


# Merge K Sorted Lists
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeKLists(lists):  # each list is sorted
    dummy = ListNode(0)
    curr = dummy
    pq = []
    for head in lists:
        if head:  # .val as key to make item comparable
            heappush(pq, (head.val, head))
    while heap:  # reference to next possibly smallest nodes
        node_min = heappop(pq)[1]
        curr.next = node_min
        curr = node_min
        if node_min.next:
            heappush(pq, (node_min.next.val, node_min.next))
    return dummy.next
# O(nlogk) time, O(k) space


# Smallest Range
# nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# return the smallest range that includes at least one number from each of the array
# approach: similar to Merge K Sorted Lists / Minimum Window Substring,
#           maintain a window by removing the smallest element then adding the one next to it
def smallest_range(self, nums):
    pq = []
    for i, num_arr in enumerate(nums):
        heappush(pq, (num_arr[0], i, 0))  # value, i, j

    values = [num_arr[0] for num_arr in nums]
    left, right = min(values), max(values)  # current min/max
    ans = left, right  # global range

    while pq:
        # get the number after current minimum and push it to heap
        _, i, j = heappop(pq)

        if j == len(nums[i]) - 1:
            break

        new_val = nums[i][j+1]
        heappush(pq, (new_val, i, j + 1))
        # update current and global min/max
        left = pq[0][0]
        right = max(right, new_val)

        if right - left < ans[1] - ans[0]:
            ans = left, right

    return ans
# O(nlogm) time, O(m) space


# Meeting Rooms II
# given an array of intervals, find the minimum number of conference rooms required
# each interval object has .start and .end attributes
def min_meeting_rooms(self, intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda i: i.start)
    heap = [(intervals[0].end, intervals[0])]

    for i in range(1, len(intervals)):
        if heap[0][0] <= intervals[i].start:
            heappop(heap)
        heappush(heap, (intervals[i].end, intervals[i]))

    return len(heap)
# thought process:
# => minimum number of rooms requires meetings in each room has minimal idle time
# => keep track of each room's current end time
# => if the earliest end time is later than candidate meeting's start time, add a new room
# => if not, update the room with earliset end time with candidate meeting's end time
# O(nlogn) time, O(n) space


# Nth Ugly Number
def nth_ugly_number_pq(n):
    if n == 1:
        return 1
    pq = [1]
    for _ in range(1, n):
        minimum = heappop(pq)
        while pq and pq[0] == minimum:
            heappop(pq)
        heappush(pq, minimum * 2)
        heappush(pq, minimum * 3)
        heappush(pq, minimum * 5)
        # print(pq)
    return pq[0]
# O(nlogn) time, O(n) space


# find median in a stream
class MedianFinder:

    def __init__(self):
        self.lower = []  # inverted max heap [-3, -2, -1]
        self.upper = []  # min heap          [4, 5, 6]

    def addNum(self, num):
        # len(self.lower) always smaller than or equal to len(self.upper)
        if len(self.lower) == len(self.upper):
            heappush(self.lower, -num)
            ele = heappop(self.lower)
            heappush(self.upper, -ele)
        else:
            heappush(self.upper, num)
            ele = heappop(self.upper)
            heappush(self.lower, -ele)
    # O(logn) time


    def findMedian(self):
        if len(self.lower) == len(self.upper):
            return (self.upper[0] - self.lower[0]) / 2.0
        else:
            return float(self.upper[0])
    # O(1) time


# Top K Frequent Words
class Element(object):
    def __init__(self, cnt, word):
        self.cnt = cnt
        self.word = word

    # for descending count but ascending order word
    def __cmp__(self, other):
        if self.cnt == other.cnt:
            if self.word < other.word:
                return 1
            elif self.word > other.word:
                return -1
            return 0
        return self.cnt - other.cnt


def top_k_frequent(words, k):
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    pq = []
    for word, cnt in counter.iteritems():
        heappush(pq, Element(cnt, word))
        if len(pq) > k:
            heappop(pq)

    result = [None] * k
    for i in range(k):
        result[k-i-1] = heappop(pq).word
    return result
# O(nlogk) time, O(n) space