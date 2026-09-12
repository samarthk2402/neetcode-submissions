class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a frequency map for each integer
        int_count = {}
        buckets = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            int_count[nums[i]] = 1 + int_count.get(nums[i], 0)

        for num, count in int_count.items():
            buckets[count].append(num)

        # top k out of the buckets
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res