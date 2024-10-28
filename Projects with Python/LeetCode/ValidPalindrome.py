class Solution:
    def isPalindrome(self, s: str) -> bool:

        auxiliary = ''

        for c in s:
            if c.isalpha():
                auxiliary += c.lower()
            if c.isdigit():
                auxiliary += c
        if auxiliary == auxiliary[::-1]:
            return True
        
        return False

# O(n) - time
# O(n) - memory
solution = Solution()

print(solution.isPalindrome("A man, a plan, a canal: Panama"))