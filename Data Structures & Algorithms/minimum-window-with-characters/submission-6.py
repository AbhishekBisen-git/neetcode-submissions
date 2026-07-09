class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = {}
        d2 = {}

        start = 0
        left = 0
        l = float("inf")

        # build hashmap for t
        for i in range(len(t)):
            if t[i] not in d1:
                d1[t[i]] = 1
            else:
                d1[t[i]] += 1

        # sliding window on s
        for right in range(len(s)):

            if s[right] not in d2:
                d2[s[right]] = 1
            else:
                d2[s[right]] += 1

            # while current window contains all chars of t
            while all(key in d2 and d2[key] >= value for key, value in d1.items()):

                # save smallest valid window
                if right - left + 1 < l:
                    l = right - left + 1
                    start = left

                # shrink from left
                if d2[s[left]] == 1:
                    d2.pop(s[left])
                else:
                    d2[s[left]] -= 1

                left += 1

        # no valid window found
        if l == float("inf"):
            return ""

        return s[start:start + l]