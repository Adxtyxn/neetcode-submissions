from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nums={}
        for s in strs:
            key=tuple(sorted(Counter(s).items()))
            if key not in nums:
                nums[key]=[]
            nums[key].append(s)
        return list(nums.values())