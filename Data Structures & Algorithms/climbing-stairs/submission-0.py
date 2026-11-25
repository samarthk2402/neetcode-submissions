class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0 for i in range(46)]
        ways[0] = 1

        for i in range(1, n+1):
            # either take 1 step
            after_one = ways[i-1]
            # or take 2 step
            after_two = ways[i-2]
            ways[i] = after_one + after_two
        
        return ways[n]
