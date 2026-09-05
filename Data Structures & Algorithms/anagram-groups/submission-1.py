class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hash map to store previous anagrams
        anagram_to_strings = {}

        # for each new string check if in anagrams
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagram_to_strings.keys():
                anagram_to_strings[sorted_string].append(string)
            else:
                anagram_to_strings[sorted_string] = [string]

        return list(anagram_to_strings.values())
            