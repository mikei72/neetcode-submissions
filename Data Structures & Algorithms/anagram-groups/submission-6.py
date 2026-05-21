class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            key = ''.join(sorted(str))
            result[key].append(str)

        return list(result.values())
            