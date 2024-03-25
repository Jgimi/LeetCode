class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        vowels_list = []

        for i in s:
            if i in vowels:
                vowels_list.append(i)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowels_list.pop()
                
        return ''.join(s)
        