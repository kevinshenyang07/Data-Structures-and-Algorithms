# things to handle:
# surrounding whitespace chars
# + or - sign
# letters following digits can be ignored
# integer should be within int range
# return 0 for invalid input
def my_atoi(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    chars = list(s)

    sign = -1 if chars[0] == '-' else 1
    if chars[0] in ['+', '-']:
        del chars[0]

    res, i = 0, 0
    digits = '0123456789'
    while i < len(chars) and chars[i] in digits:
        res = res * 10 + digits.index(chars[i])
        i += 1

    # return val in the range of [INT_MIN, INT_MAX]
    return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


# Valid Number
def is_numeric(s):
    # define a DFA
    # type of char => state
    state = [{},
             {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
             {'digit': 3, '.': 4},
             {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
             {'digit': 5},
             {'digit': 5, 'e': 6, 'blank': 9},
             {'sign': 7, 'digit': 8},
             {'digit': 8},
             {'digit': 8, 'blank': 9},
             {'blank': 9}]
    current_state = 1
    # recognize the type of each char
    for c in s:
        if c >= '0' and c <= '9':
            c = 'digit'
        if c == ' ':
            c = 'blank'
        if c in ['+', '-']:
            c = 'sign'
        if c not in state[current_state].keys():
            return False
        # jump to a new state
        current_state = state[current_state][c]
    # is numeric only if the final state is in the following
    if current_state not in [3, 5, 8, 9]:
        return False
    return True


# Roman Numeral
# I: 1, V:5, X:10, L: 50, C: 100, D: 500, M: 1000
# only one char is allowed to put on the left to represent subtration
# only use subtracton between two digits or on the same digit
# for example, 499 = 400 + 90 + 9 = CD + XC + IX != ID

# Roman to Integer
# the range of the value is [1, 4000)
def roman_to_int(s):
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
    res = 0
    for i, c in enumerate(s):
        if i < len(s) - 1 and mapping[s[i]] < mapping[s[i + 1]]:
            res -= mapping[s[i]]
        else:
            res += mapping[s[i]]
    return res


# Integer to Roman
# the range of the value is [1, 4000)
def int_to_roman(num):
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10]
