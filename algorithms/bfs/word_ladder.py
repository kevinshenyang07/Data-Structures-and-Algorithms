import string

# Word Ladder
class Solution(object):
    def ladder_length(begin_word, end_word, word_list):
        # all the words after begin_word need to be in word list
        if end_word not in word_list:
            return 0
        length = 2
        left, right = set([begin_word]), set([end_word])
        word_set = set(word_list)
        # two-end BFS
        while left:
            left = get_adj_words(left, word_set)
            if left & right:
                return length
            length += 1
            # swap to generate smaller set
            if len(left) > len(right):
                left, right = right, left
            # avoid cycle
            # only remove the words in the left when the left is determined
            # since left is end of current path
            word_set -= left
        return 0

    def get_adj_words(source_words, word_set):
        adj_words = set([])
        for word in source_words:
            for i in range(len(word)):
                for char in string.lowercase:
                    candidate_word = word[:i] + char + word[i+1:]
                    if candidate_word in word_set:
                        adj_words.add(candidate_word)
        return adj_words
