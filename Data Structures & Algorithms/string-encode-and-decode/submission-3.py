class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            if len(string) < 10:
                encoded += "00" + str(len(string)) + string
            elif len(string) < 100:
                encoded += "0" + str(len(string)) + string
            else:
                encoded += str(len(string)) + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        if len(s) <= 0:
            return []
        digits = 3
        count = 0
        i = 0

        while i < len(s):
            if digits > 0 :
                count = int(s[i:i+digits])
                i = i+digits
                digits = 0
                if count == 0:
                    decoded.append("")
                    digits = 3
            else:
                
                decoded.append(s[i:i+count])
                i = i+count
                digits = 3
            

        return decoded