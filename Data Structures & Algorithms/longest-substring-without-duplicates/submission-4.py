class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        curr = 0
        max_l = 0
        char_set = set({})

        # extend right pointer till duplicate found
        while r < len(s) and l <= r:
            if s[r] in char_set:
                # end of substring
                max_l = max(curr, max_l)
                char_set.remove(s[l])
                l += 1
                curr = r-l
            else:
                char_set.add(s[r])
                curr += 1
                r += 1

        if curr > 0:
            max_l = max(curr, max_l)
        
        return max_l