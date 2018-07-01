# a valid IP address format would be xxx.xxx.xxx.xxx
# where xxx is an integer from 0 to 255
def restore_IP_addresses(s):
    '''
    :type s: str, e.g. '19216801'
    :rtype: List[str], all valid IP addresses
    '''
    def dfs(depth, substr, path):
        if depth == 4 and substr == '':
            result.append('.'.join(path))
            return
        if depth == 4 or substr == '':
            return
        for i in range(1, min(len(substr) + 1, 4)):
            addr = substr[:i]
            if int(addr) > 255:
                continue
            if len(addr) > 1 and addr[0] == '0':
                continue  # pass addresses like '09'
            dfs(depth + 1, substr[i:], path + [addr])
    result = []
    dfs(0, s, [])
    return result
