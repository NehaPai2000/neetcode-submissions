class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Brute force
        maxL=[]
        l=0
        r=0
        max2=float('-inf')
        while r<len(nums):
            maxe = max2
            max2=float('-inf')
            r=l
            count=0
            while (r-l)<k:
                 if count>0:
                    max2=max(max2,nums[r])
                 maxe=max(maxe,nums[r])
                 r+=1
                 count+=1
            maxL.append(maxe)
            l+=1
        return maxL