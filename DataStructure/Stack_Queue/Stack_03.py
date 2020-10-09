class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        for today, temp in enumerate(T):
            while stack:
                past_day, past_temp = stack[-1]
                if past_temp < temp:
                    T[past_day] = today - past_day
                    stack.pop()
                else:
                    break
            stack.append((today, temp))
        for rest in stack:
            T[rest[0]] = 0
        return T