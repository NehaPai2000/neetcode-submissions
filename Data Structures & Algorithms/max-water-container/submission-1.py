class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxp=-1
        while i<j:
            product=(j-i)*min(heights[j],heights[i])
            maxp=max(maxp,product)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return maxp

