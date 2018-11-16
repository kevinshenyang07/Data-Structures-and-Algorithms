import collections

# when typing in IDE, a list of matching files are provided
# and the list can be narrowed with each key stroke
# for example, when user input is my<pause>f<pause>p<pause>
# 1st call: matched_files('my'), 2nd call: matched_files('myf'), 3rd cal: matched_files('myfp')
# find an efficient implementation when the total number of files is very large
def get_all_files():
    return ['my_func.py', 'my_fetcher.py', 'my_crawler.py', 'my_parser.py', '__init__.py']

class FileFinder(object):
    def __init__(self):
        self.cache = collections.defaultdict(list)  # pattern => (fname, starting idx)
        self.cache[''] = [(fname, 0) for fname in get_all_files()]

    def matched_files(self, pattern):
        # look for 'myfp' => 'myf' => 'my' => 'm' => ''
        for i in range(len(pattern), -1, -1):
            p = pattern[:i]
            if p in self.cache:
                subset = self.get_subset(self.cache[p], pattern[i:])
                self.cache[pattern] = subset
                return [fname for fname, _ in subset]

    def get_subset(self, pairs, pattern):
        subset = []
        for fname, i in pairs:
            j = self.is_subsequence(pattern, fname, i)
            if j >= 0:
                subset.append((fname, j))
        return subset

    def is_subsequence(self, pattern, target, starting_idx):
        # not enough chars to match
        if len(pattern) > len(target) - starting_idx:
            return -1
        i, j = 0, starting_idx
        while i < len(pattern) and j < len(target):
            if pattern[i] == target[j]:
                i += 1
            j += 1
        if i < len(pattern) and j == len(target):
            return -1
        return j


if __name__ == '__main__':
    file_finder = FileFinder()

    patterns = ['', 'm', 'myf', 'myfp', 'init']
    for p in patterns:
        print file_finder.matched_files(p)

