# <Evaluate Reverse Polish Notation>
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                result = self.operate(op1, op2, token)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()

    def operate(self, op1, op2, operator):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        else:
            return int(op1 / op2)   

