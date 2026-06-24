class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        res = 0

        for c in s:
            if c in char_set:
                char_set.remove(c)
                res += 2
            else:
                char_set.add(c)
            
        if char_set:
            res += 1
        return res