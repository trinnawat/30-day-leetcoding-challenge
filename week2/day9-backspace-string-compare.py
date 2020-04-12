'''
    https://leetcode.com/problems/backspace-string-compare
'''


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while True:
            try:
                idx = S.index('#')
                if idx == 0:
                    S = S[1:]
                else:
                    S = S[:idx-1] + S[idx+1:]
                idx2 = T.index('#')
                if idx2 == 0:
                    T = T[1:]
                else:
                    T = T[:idx2-1] + T[idx2+1:]
            except:
                break
        if len(S) > len(T):
            F = S
            N = T
        else:
            F = T
            N = S
        while True:
            try:
                idx = F.index('#')
                if idx == 0:
                    F = F[1:]
                else:
                    F = F[:idx-1] + F[idx+1:]
            except:
                break
        return F == N
