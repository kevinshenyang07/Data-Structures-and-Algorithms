# Remove Comments
# cases:
# 1. line comment
# 2. block comment in a line
# 3. block comment in multiple line (might have chars across lines)
#    e.g. ["a/*comment", "line", "more_comment*/b"] => ["ab"]
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        block = False
        formatted = []

        for s in source:
            chars = []
            i = 0
            while i < len(s):
                # start of line comment
                if s[i:i+2] == '//' and not block:
                    i = len(s) # advance pointer to end of current s
                # start of block comment
                elif s[i:i+2] == '/*' and not block:
                    block = True
                    i += 1  # skip current char
                # end of block comment
                elif s[i:i+2] == '*/' and block:
                    block = False
                    i += 1  # skip current char
                # normal character
                elif not block:
                    chars.append(s[i])
                # else: part of block comment
                i += 1

            if chars and not block:  # block not finished
                formatted.append(''.join(chars))

        return formatted
