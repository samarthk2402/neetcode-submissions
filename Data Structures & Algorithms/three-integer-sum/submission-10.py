class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums [i-1]:
                continue
            l = i+1
            r = len(nums) - 1

            while r > l:
                sum = nums[r] + nums[l] + nums[i]
                if sum == 0:
                    if [nums[r], nums[l], nums[i]] not in triplets:
                        triplets.append([nums[r], nums[l], nums[i]])

                    r -= 1
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1

        return triplets

            