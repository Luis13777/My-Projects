class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        chance = True

        while (left < right):
            if (s[left] == s[right]):
                left += 1
                right -= 1
            else:
                if chance:
                    chance = False

                    if (right - left == 1):
                        return True

                    if (s[left+1] != s[right] and s[left] != s[right-1]):
                        return False
                    elif (s[left+1] != s[right] and s[left] == s[right-1]):
                        right -= 1
                    elif (s[left+1] == s[right] and s[left] != s[right-1]):
                        left += 1
                    else:
                        s1 = s[left:right:1]
                        s2 = s[left + 1:right+1:1]

                        if self.isPalindrome(s1) or self.isPalindrome(s2):
                            return True
                        return False
                else:
                    return False
        return True
                
    def isPalindrome (self, s: str):
        if s == s[::-1]:
            return True
        return False    
    
# O(n)
                        