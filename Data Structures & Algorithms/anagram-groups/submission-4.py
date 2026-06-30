class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            SortedStr = ''.join(sorted(s))
            res[SortedStr].append(s)
        return list(res.values())