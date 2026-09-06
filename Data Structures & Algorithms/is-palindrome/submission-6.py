class Solution:

    def is_alphanumeric(self, char):
        if not char.isalpha() and not char.isdigit():
            return False
        else:
            return True

    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            while not self.is_alphanumeric(s[start]) and start < len(s) -1:
                start += 1
            while not self.is_alphanumeric(s[end]) and end > 0:
                end -= 1

            if self.is_alphanumeric(s[start]) and self.is_alphanumeric(s[end]) and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True
