class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        size = len(string)
        i = 0
        while (i<size/2):
            if (string[i]!=string[size-i-1]):
                return False
            i += 1
        return True

sol = Solution()

print(sol.isPalindrome(121))