class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for str in strs:
            temp = ''.join(sorted(list(str)))
            if(temp in mapping):
                mapping[temp].append(str)
            else:
                mapping[temp] = [str]
        res = []
        for arr in mapping.values():
            res.append(arr)
        return res