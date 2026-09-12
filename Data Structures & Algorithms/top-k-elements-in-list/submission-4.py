class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a frequency map for each integer
        int_count = {}
        for i in range(len(nums)):
            int_count[nums[i]] = 1 + int_count.get(nums[i], 0)

        # sort frequency map

        int_count = sorted(int_count, key = lambda x: int_count[x], reverse=True)

        return int_count[:k]