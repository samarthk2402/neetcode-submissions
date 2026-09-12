class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        curr = 0
        max_l = 0

        # extend right pointer till duplicate found
        while r < len(s) and l <= r:
            if s[r] in s[l:r]:
                # end of substring
                max_l = max(curr, max_l)
                l += 1
                curr = r-l
            else:
                curr += 1
                r += 1

        if curr > 0:
            max_l = max(curr, max_l)
        
        return max_l