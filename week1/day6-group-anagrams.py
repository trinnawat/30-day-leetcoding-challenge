'''
    https://leetcode.com/problems/group-anagrams/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for s in strs:
            sr = tuple(sorted(s))
            if sr not in results:
                results[sr] = []
            results[sr].append(s)
        return list(results.values())