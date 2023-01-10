from collections import Counter #Counter preserves order of elements during insertions
class Solution:
    def firstUniqChar(self, s: str):
        for i,j in Counter(s).items():
            if j == 1:
                return s.index(i)
        return -1

