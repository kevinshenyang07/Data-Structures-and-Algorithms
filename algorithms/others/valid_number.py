# Valid Number
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        has_number = False
        has_point = False
        has_e = False
        number_after_e = True

        for i, char in enumerate(s):
            if char in '0123456789':
                has_number = True
                number_after_e = True
            elif char == '.':
                if has_e or has_point:
                    return False
                has_point = True
            elif char == 'e':
                if has_e or not has_number:
                    return False
                number_after_e = False
                has_e = True
            elif char in '+-':
                if i != 0 and s[i - 1] != 'e':
                    return False
            else:
                return False

        return has_number and number_after_e

# Thought Process
# 1. find out all possible chars
#    " .+-e0123456789"
# 2. list examples
#    valid: "0", "1.2", "-1", "2e10", "0.2", "2e-10"
#    not valid: "1. 2", "2e.10", "2-e10", "2e10e10"
# 3. find out rules
#    " " can only be at beginning or end
#    ".0123456789" can be anywhere
#    "+-" can only be at beginning or after "e"
#    "e" must have number before and after
#    "e" can not have more than one occurrence
#    "." can not be after "e"
#    "." can not have more than one occurrence
