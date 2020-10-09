class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chrMap = {
        '(': ('open', 0),
        ')': ('close', 0),
        '{': ('open', 1),
        '}': ('close', 1),
        '[': ('open', 2),
        ']': ('close', 2),
        }
        stack = []
        for ch in s:
            newBrackets = chrMap[ch]
            if newBrackets[0] == 'open':
                stack.append(newBrackets)
            else:
                if len(stack) == 0 :
                    return False
                brackets = stack.pop()
                if brackets[1] != newBrackets[1]:
                    return False
        if len(stack) != 0:
            return False
        return True