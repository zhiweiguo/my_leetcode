# 每日打卡 day6 : 820

'''
单词的压缩编码

'''

# 定义字典树中的一个节点
class Node(object):
    def __init__(self):
        self.children={}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:        
        words = list(set(words))   # 去重
        trie = Node() # 根节点，空
        nodes = []
        ans = 0
        for word in words:
            now = trie
            for char in reversed(word):
                if char not in now.children:
                    now.children[char] = Node()
                now = now.children[char]
            nodes.append(now)

        for w, c in zip(words, nodes):
            if len(c.children) == 0:
                ans += len(w) + 1
        
        return ans



