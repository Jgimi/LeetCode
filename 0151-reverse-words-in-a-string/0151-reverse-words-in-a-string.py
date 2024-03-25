class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join(list(filter(None, list(s.split(' '))))[::-1])
        return s
        