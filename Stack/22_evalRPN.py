# https://leetcode.com/problems/evaluate-reverse-polish-notation/

"""
Stack-Based Evaluation: The algorithm uses a stack to handle operands and operators as per the rules of Reverse Polish Notation (RPN).

Handling Operators: For each operator (+, -, *, /):

Pop the top two numbers from the stack.
Perform the operation.
Push the result back onto the stack.
Handling Numbers: If the token is a number, simply push it onto the stack.

Final Result: After processing all tokens, the stack should contain one element, which is the final result.

Time Complexity: O(n)
Space Complexity: O(n)
"""

""""
Try to dry run with random example. 
"""


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initialize an empty stack to store operands

        # Iterate through each token in the input list
        for ch in tokens:
            # If the token is an operator, pop two elements from the stack, perform the operation, and push the result
            if ch == "+":
                a = stack.pop()  # Pop the last operand
                b = stack.pop()  # Pop the second-last operand
                ans = a + b  # Perform addition
                stack.append(ans)  # Push result back to the stack

            elif ch == "-":
                a = stack.pop()
                b = stack.pop()
                ans = b - a  # Perform subtraction (order matters)
                stack.append(ans)

            elif ch == "*":
                a = stack.pop()
                b = stack.pop()
                ans = b * a  # Perform multiplication
                stack.append(ans)

            elif ch == "/":
                a = stack.pop()
                b = stack.pop()
                ans = int(
                    b / a
                )  # Perform integer division and ensure truncation toward zero
                stack.append(ans)

            # If the token is a number, convert it to an integer and push it onto the stack
            else:
                num = int(ch)
                stack.append(num)

        # The final result will be the only element left in the stack
        return stack[0]
