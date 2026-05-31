class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        s=[]
        sorted_hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)
        for key, value in sorted_hm[:k]:
             s.append(key)
        return s

