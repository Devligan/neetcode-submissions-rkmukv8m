class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            if(num in mapping):
                mapping[num] += 1
            else:
                mapping[num] = 1
        return sorted(mapping, key = mapping.get)[-k:]