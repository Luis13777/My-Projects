class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        l = 0
        r = 0
        current = 0
        maximun = 0
        Set = set()
        while (r < len(s)):
            if s[r] not in Set:
                Set.add(s[r])
                r += 1
            else:
                current = r - l
                if (current > maximun):
                    maximun = current
                while (s[l] != s[r]):
                    Set.remove(s[l])
                    l += 1
                l += 1
                r += 1
            if (r == len(s)):
                current = r - l
                if (current > maximun):
                    maximun = current 
        return maximun

solution = Solution()

print(solution.lengthOfLongestSubstring("a"))
    
