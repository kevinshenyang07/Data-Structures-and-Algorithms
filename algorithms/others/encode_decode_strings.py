# Encode and Decode Strings
# The string may contain any possible characters out of 256 valid ascii characters.
# Both encode and decode methods should be stateless.
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(str(len(s)) + ':' + s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)  # first index after i
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs
