# f(["a","b","b","b","b","b","b","b","b","b","b","c","c"]) = ["a","b","1","0","c","2"]
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)
        # i - end of compressed string
        # j - start of unchecked chars
        i = j = 0
        while j < len(chars):
            curr = chars[j]
            count = 0
            # count repeating chars
            while j < len(chars) and chars[j] == curr:
                j += 1
                count += 1
            # write the char to be compressed
            chars[i] = curr
            # write the times repeated
            if count > 1:
                for digit in str(count):
                    i += 1
                    chars[i] = digit
            i += 1

        return i
# O(n) time, O(1) space
