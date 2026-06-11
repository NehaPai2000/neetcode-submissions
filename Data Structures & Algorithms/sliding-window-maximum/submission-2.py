class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxL=[]
        l=0
        r=0
        
        while r<len(nums):
            maxe = float('-inf')
            r=l
            while (r-l)<k:
                 maxe=max(maxe,nums[r])
                 r+=1
            maxL.append(maxe)
            l+=1
        return maxL