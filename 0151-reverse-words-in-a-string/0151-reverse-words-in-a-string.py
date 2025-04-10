class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.strip().split()
        reversed_word = word[::-1]

        return ' '.join(reversed_word)