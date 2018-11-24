# Input: "I am {0} {2}.", {"very", "apple", "happy"}, Output: "I am very happy."
# list out all corner case.
# assumption:
# 1. no implicit indexing like '{}'
# 2. brackets always expect a valid index inside
def format_str(s, words):
    subs = []  # (i, j, word_idx)
    stack = []  # index of open bracket

    for i, char in enumerate(s):
        if not stack and char != '{':
            continue
        if char == '{':
            stack.append(i)
        elif char == '}':
            # take everything inside
            start = stack[-1]
            idx_str = s[start + 1:i]
            if valid_int(idx_str):
                subs.append((start, i, int(idx_str)))
            else:
                return 'KeyError'

    if not subs:
        return s

    chars = []
    j = 0
    for i, char in enumerate(s):
        start, end, word_idx = subs[j]

        if j >= len(subs) or i < start:
            chars.append(char)
        elif i == start:
            if word_idx >= len(words):
                return 'IndexError'
            for word_char in words[word_idx]:
                chars.append(word_char)
        elif i == end:
            j += 1

    return ''.join(chars)

def valid_int(s):
    try:
        int(s)
        return True
    except:
        return False

def test():
    words = ['very', 'apple', 'happy']
    print format_str(r'a', words)  # 'a'
    print format_str(r'{', words)  # '{'
    print format_str(r'}', words)  # '}'
    print format_str(r'{0', words)  # '{0'
    print format_str(r'{a', words)  # '{a'
    print format_str(r'{{', words)  # '{{'
    print format_str(r'{9}', words)  # 'Index Error'
    print format_str(r'{-1}', words)  # 'happy'
    print format_str(r'{a}', words)  # 'Key Error'
    print format_str(r'{{0} {1}}', words)  # 'Key Error'
    print format_str(r'{0} {2}', words)  # 'very happy'
    print format_str(r'{0} {0}', words)  # 'very very'
    print format_str(r'{10}', words * 4)  # 'apple'


if __name__ == '__main__':
    test()
