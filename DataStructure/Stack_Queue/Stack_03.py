# <Daily Temperatures>
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

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