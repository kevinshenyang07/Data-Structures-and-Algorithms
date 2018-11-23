# there is no guarantee of find the secret word in 10 guesses
# for example ['aaaaaa', 'bbbbbb', ..., 'zzzzzz']
# the strategy really depends on the distribution of chars
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        while True:
            picked = self.most_connected_word(wordlist)
            n = master.guess(picked)

            if n == len(picked):
                return
            # the secret word must be among the words that also share n chars with picked
            wordlist = [w for w in wordlist if self.similarity(w, picked) == n]

    # for each word, count how many other words have 0 similarity
    def most_connected_word(self, wordlist):
        counter = {}
        for w1 in wordlist:
            counter[w1] = counter.get(w1, 0)
            for w2 in wordlist:
                if self.similarity(w1, w2) > 0:
                    counter[w1] += 1
        return max(wordlist, key=lambda w: counter[w])

    def similarity(self, w1, w2):
        sim = 0
        for i in range(min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                sim += 1
        return sim
