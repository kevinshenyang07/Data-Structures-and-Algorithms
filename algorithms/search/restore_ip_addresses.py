# a valid IP address format would be xxx.xxx.xxx.xxx
# where xxx is an integer from 0 to 255
def restore_IP_addresses(s):
    '''
    :type s: str, e.g. '19216801'
    :rtype: List[str], all valid IP addresses
    '''
    def dfs(depth, sub_str, path):
        # stop when too many chars are left
        if len(sub_str) > (4 - depth) * 3:
            return
        # end case
        if depth == 4:
            result.append(path)
            return
        # limit iteration range
        max_length = min(3, len(sub_str))
        for i in range(max_length):
            partial = sub_str[:i + 1]
            if int(partial) > 255:
                continue
            # if partial has two digits but starts with 0
            if i > 0 and sub_str[0] == '0':
                continue
            dfs(depth + 1, sub_str[i + 1:], path + [partial])

    result = []
    dfs(0, s, [])
    return ['.'.join(r) for r in result]
