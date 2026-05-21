class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            key = sorted(str)
            result[tuple(key)].append(str)

        return list(result.values())
            