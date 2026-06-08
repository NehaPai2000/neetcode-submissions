class Solution:
    def trap(self, height: List[int]) -> int:
        maxl=height[0]
        maxr=height[len(height)-1]
        maxleft=[0]*len(height)
        maxright=[0]*len(height)
        maxleft[0]=height[0]
        maxright[len(height)-1]=height[len(height)-1]
        area=0
        for i in range(1,len(height)):
            maxleft[i]=max(maxleft[i-1],maxl)
            maxl=max(maxl,height[i])
        for i in range(len(height)-2,-1,-1):
            maxright[i]=max(maxright[i+1],maxr)
            maxr=max(maxr,height[i])
        for i in range(1,len(height)):
            if min(maxleft[i],maxright[i])<height[i]:
                area+=0
            else:
                area+=min(maxleft[i],maxright[i])-height[i]
        return area

            