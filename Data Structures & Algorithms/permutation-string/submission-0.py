class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count=[0]*26
        for i in s1:
            count[ord(i)-ord('a')]+=1
        
        l=0
        
        
        for r in range(len(s2)):
            count[ord(s2[r]) - ord('a')] -= 1

            if r - l + 1 > len(s1):
                count[ord(s2[l]) - ord('a')] += 1
                l += 1

            if all(x == 0 for x in count):
                return True

        return False