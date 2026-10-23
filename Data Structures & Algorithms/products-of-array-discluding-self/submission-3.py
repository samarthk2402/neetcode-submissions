class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 0

        zeros = 0
        for num in nums:
            if num != 0:
                if product == 0:
                    product = num
                else:
                    product = product*num
            else:
                zeros+= 1

        result = []
        for num in nums:
            if zeros > 1:
                result.append(0)
            elif zeros == 1:

                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                if num == 0:
                    result.append(product)
                else:
                    result.append(product//num)

        return result