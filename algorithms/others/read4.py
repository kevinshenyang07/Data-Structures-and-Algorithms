# Read N Characters Given Read4 II - Call multiple times
# API: int read4(char *buf) reads 4 characters at a time from a file.
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
# Note: The read function may be called multiple times.
# Exmaple:
# Given buf = "abc"
# read("abc", 1) // returns "a"
# read("abc", 2); // returns "bc"
# read("abc", 1); // returns ""
class Solution(object):
    def __init__(self):
        # to cache the extra chars read from last call of read4()
        self.queue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total_read = 0
        eof = False
        tmp = [''] * 4

        while total_read < n and not eof:
            # tmp will be modified in place
            curr_read = read4(tmp)
            eof = curr_read < 4

            for i in range(curr_read):
                self.queue.append(tmp[i])

            length = min(n - total_read, len(self.queue))

            for i in range(length):
                buf[total_read] = self.queue.pop(0)
                total_read += 1

        return total_read
