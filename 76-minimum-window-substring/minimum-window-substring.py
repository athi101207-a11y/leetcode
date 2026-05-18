from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        result = [-1, -1]
        min_length = float("inf")

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            # Try shrinking window
            while have == need_count:

                # Update result
                if (right - left + 1) < min_length:
                    result = [left, right]
                    min_length = right - left + 1

                # Remove left character
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        left, right = result

        return s[left:right + 1] if min_length != float("inf") else ""