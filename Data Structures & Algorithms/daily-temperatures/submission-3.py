class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        waiting = []

        for i in range(len(temperatures)):

            while len(waiting)>0 and temperatures[i] > temperatures[waiting[-1]]:
                result[waiting[-1]] = i - waiting[-1]
                waiting.pop()
                 
            waiting.append(i)

        return result


