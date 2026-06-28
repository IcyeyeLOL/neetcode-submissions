class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            SortedStrings = ''.join(sorted(s))
            res[SortedStrings].append(s)
        return list(res.values())
        