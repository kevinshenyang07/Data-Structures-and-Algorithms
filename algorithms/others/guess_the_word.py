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
            counter = self.count_zero_similarities(wordlist)
            # the word that is 'connected' to most words
            picked = min(wordlist, key=lambda w: counter[w])
            n = master.guess(picked)

            if n == len(picked):
                return
            # the secret word must be among the words that also share n chars with picked
            wordlist = [w for w in wordlist if self.similarity(w, picked) == n]

    # for each word, count how many other words have 0 similarity
    def count_zero_similarities(self, wordlist):
        counter = {}
        for w1 in wordlist:
            counter[w1] = counter.get(w1, 0)
            for w2 in wordlist:
                if self.similarity(w1, w2) == 0:
                    counter[w1] += 1
        return counter

    def similarity(self, w1, w2):
        sim = 0
        for i in range(min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                sim += 1
        return sim
