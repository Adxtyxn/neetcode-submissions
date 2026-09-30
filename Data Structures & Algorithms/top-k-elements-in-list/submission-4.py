from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        count=dict(sorted(Counter(nums).items(),key=lambda x:x[1],reverse=True))
        keys=list(count.keys())
        for i in range(k):
            res.append(keys[i])
        return res