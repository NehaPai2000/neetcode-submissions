class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        s=[0]*(len(nums)+1)
        #sorted_hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)
        #for key, value in sorted_hm[:k]:
        #     s.append(key)
    #    return s
        for i in hm:
             if s[hm[i]]==0:
                s[hm[i]]=[i]
             else:
                s[hm[i]].append(i)
        res = []

        for i in range(len(s) - 1, 0, -1):
            if s[i] != 0:
                for j in s[i]:
                    res.append(j)

                    if len(res) == k:
                        return res

