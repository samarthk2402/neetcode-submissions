class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_to_count = {}

        for char in s:
            if char not in letter_to_count:
                letter_to_count[char] = 1
            else:
                letter_to_count[char] += 1

        for char in t:
            if char not in letter_to_count:
                return False
            if letter_to_count[char] >= 1:
                letter_to_count[char] -= 1
            else:
                return False

        if sum(letter_to_count.values()) == 0:
            return True
        else:
            return False