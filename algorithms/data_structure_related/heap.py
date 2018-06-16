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
        self.heaps = [], []

    def addNum(self, num):
        max_pq, min_pq = self.heaps
        # push to min_pq, get the minimum, then push to max_pq
        heappush(min_pq, num)
        ele = heappop(min_pq)
        heappush(max_pq, -ele)
        # keep the balance between max_pq and min_pq
        if len(max_pq) > len(min_pq):
            # move one ele from max_pq to min_pq
            ele = heappop(max_pq)
            heappush(min_pq, -ele)

    def findMedian(self):
        max_pq, min_pq = self.heaps
        if len(max_pq) < len(min_pq):
            return float(min_pq[0])
        return (min_pq[0] - max_pq[0]) / 2.0


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