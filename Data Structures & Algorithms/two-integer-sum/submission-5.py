class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index[num] = i

        for i in range(len(nums)):
            rem = target - nums[i]

            if num_to_index.get(rem, False) and i != num_to_index[rem]:
                return [i, num_to_index[rem]]
