'''
    Perform String Shifts

    You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
    - direction can be 0 (for left shift) or 1 (for right shift). 
    - amount is the amount by which string s is to be shifted.
    - A left shift by 1 means remove the first character of s and append it to the end.
    - Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
    Return the final string after all operations
'''


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for cmd in shift:
            # 0 left, 1 right
            command = cmd[0]
            num_shift = cmd[1]
            if command == 0:
                total_shift += num_shift
            else:
                total_shift -= num_shift
        if total_shift % len(s) == 0:
            return s
        else:
            total_shift = total_shift % len(s)
            return s[total_shift:] + s[:total_shift]
        return shift_s
