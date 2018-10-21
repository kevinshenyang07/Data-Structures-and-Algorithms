class QueueWithMax(object):

    def __init__(self):
        self.queue = collections.deque()
        self.max_queue = collections.deque()

    def enqueue(self, ele):
        self.queue.append(ele)
        if self.max_queue != []:
            while self.max_queue and self.max_queue[-1] < ele:
                self.max_queue.pop()
        self.max_queue.append(ele)

    def dequeue(self):
        if self.queue == []:
            raise ValueError('dequeue from empty queue')
        ele = self.queue.popleft()
        if self.max_queue[0] == ele:
            self.max_queue.popleft()
        return ele

    # O(1) amortized
    def max(self):
        if len(self.max_queue) == 0:
            return None
        else:
            return self.max_queue[0]


if __name__ == '__main__':
    qwm = QueueWithMax()
    qwm.enqueue(5)
    print 'queue: ', qwm.queue
    print 'max value: ', qwm.max()
    qwm.enqueue(1)
    qwm.enqueue(3)
    qwm.enqueue(4)
    qwm.enqueue(2)
    print 'queue: ', qwm.queue
    print 'max value: ', qwm.max()
    qwm.dequeue()
    print 'queue: ', qwm.queue
    print 'max value: ', qwm.max()
    qwm.dequeue()
    print 'queue: ', qwm.queue
    print 'max value: ', qwm.max()
    qwm.dequeue()
    print 'queue: ', qwm.queue
    print 'max value: ', qwm.max()
    qwm.dequeue()
    print 'queue: ', qwm.queue
    print 'max value: ', qwm.max()
