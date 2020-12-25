#<Valid Parentheses>
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

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

#  Better solution
#  class Solution:
#     # @return a boolean
#     def isValid(self, s):
#         stack = []
#         dict = {"]":"[", "}":"{", ")":"("}
#         for char in s:
#             if char in dict.values():
#                 stack.append(char)
#             elif char in dict.keys():
#                 if stack == [] or dict[char] != stack.pop():
#                     return False
#             else:
#                 return False
#         return stack == []