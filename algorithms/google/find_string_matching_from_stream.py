# find string matching from stream
# given a char stream with two APIs next() and hasNext(), and words List[str] as target
# whenever a target word appears in the stream, print it out
def find_matched(stream, words):
    pass

# 把词典的word逆序后建Trie树 ，再用一个vector存最近遇到的
# max_length_of_word_in_dict个char，每次来一个char就逆序构造string到Trie中查找
# 例：
# stream里已有aabca，新来一个字符t，变成aabcat。
# 字典里有"cat","bcat","aabcat"。
# 反建trie的话得到t->a->c (isWord) ->b (isWord) ->a->a (isWord)。
# aabcat从后往前遍历一次在trie里就能找到所有词。
