class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        hm = {}
        freq = 0
        maxslide = 0

        for r in range(len(s)):
            if s[r] in hm:
                hm[s[r]] += 1
            else:
                hm[s[r]] = 1

            freq = max(freq, hm[s[r]])

            while (r - l + 1) - freq > k:
                hm[s[l]] -= 1
                l += 1

            maxslide = max(maxslide, r - l + 1)

        return maxslide