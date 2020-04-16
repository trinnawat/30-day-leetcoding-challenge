'''
    https://leetcode.com/problems/valid-parenthesis-string
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            #print("C: ", c)
            if c == '(' or c == '*':
                stack.append(c)
            if c == ')':
                if len(stack) > 0:
                    try:
                        left_idx = len(stack) - 1 - stack[::-1].index('(')
                        #print("left_idx: ", left_idx)
                    except:
                        #print("Cannot find left ", stack)
                        pass
                    else:
                        stack.pop(left_idx)
                        continue

                    try:
                        star_idx = len(stack) - 1 - stack[::-1].index('*')
                        #print("star_idx: ", star_idx)
                    except:
                        #print("Cannot find star ", stack)
                        pass
                    else:
                        stack.pop(star_idx)
                        continue
                    return False
                else:
                    return False
            # print(stack)
        print('stack: ', stack)
        final_stack = []
        for c in stack:
            if c == '(':
                final_stack.append(c)
                continue
            if c == '*':
                if len(final_stack) == 0:
                    continue
                else:
                    final_stack.pop()
        return len(final_stack) == 0
