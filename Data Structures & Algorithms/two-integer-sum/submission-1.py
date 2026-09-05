class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            rem = target - num
            if rem in hash_map.keys():
                return [hash_map[rem], i]
            hash_map[num] = i 