# a valid IP address format would be xxx.xxx.xxx.xxx
# where xxx is an integer from 0 to 255
class Solution(object):
    def restoreIpAddresses(self, s):
        '''
        :type s: str, e.g. '19216801'
        :rtype: List[str], all valid IP addresses
        '''
        self.result = []
        self.dfs(0, s, [])
        return self.result

    def dfs(self, depth, substr, path):
        if depth == 4 and substr == '':
            self.result.append('.'.join(path))
            return
        if depth == 4 or substr == '':
            return

        for i in range(1, min(len(substr) + 1, 4)):
            addr = substr[:i]
            if int(addr) > 255:
                continue
            if len(addr) > 1 and addr[0] == '0':
                continue  # pass addresses like '09'
            self.dfs(depth + 1, substr[i:], path + [addr])
