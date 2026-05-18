class Solution:
    def longestPalindrome(self, s):
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            # Odd length palindrome
            temp1 = expand(i, i)

            # Even length palindrome
            temp2 = expand(i, i + 1)

            # Choose longer palindrome
            if len(temp1) > len(longest):
                longest = temp1

            if len(temp2) > len(longest):
                longest = temp2

        return longest