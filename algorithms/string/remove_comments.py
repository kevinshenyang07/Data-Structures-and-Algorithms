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
        chars = []

        for s in source:
            i = 0
            while i < len(s):
                if not block:
                    if s[i:i+2] == '//':
                        break
                    if s[i:i+2] == '/*':
                        block = True
                        i += 2
                    else:
                        chars.append(s[i])  # normal chars
                        i += 1
                else:
                    if s[i:i+2] == '*/':
                        block = False
                        i += 2
                    else:
                        i += 1  # skip chars in block

             # only append when block has finished (see case 3)
            if chars and not block:
                formatted.append(''.join(chars))
                chars = []

        return formatted
