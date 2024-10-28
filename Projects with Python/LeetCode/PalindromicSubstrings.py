class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count = 0
        for index in range(len(s)):
            count += 1
            #first case (odd substring)
            if index >= 1 and index < len(s) - 1:
                l = index - 1
                r = index + 1
                while (l >= 0 and r < len(s) and s[l] == s[r]):
                    count += 1
                    l -= 1
                    r += 1
            #second case (even substring)
            if index >= 1 and s[index] == s[index - 1]:
                count += 1
                if index >= 2 and index < len(s) - 1:
                    l = index - 2
                    r = index + 1
                    while (l >= 0 and r < len(s) and s[l] == s[r]):
                        count += 1
                        l -= 1
                        r += 1

        return count

solution = Solution()

# O(1) + O(2) + ... + O(n/2) + ... O(1)

# 1 + 2 + ... + n/2 + ... + 1 = O(n^2)

print(solution.countSubstrings("aaa"))