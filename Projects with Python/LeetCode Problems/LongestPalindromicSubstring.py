class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        answer = ''
        for i in range(len(s)):
            r = size - 1
            l = i
            if (r-l > len(answer)):
                while (r > l):
                    if s[r] != s[l]:
                        r -= 1
                    else:
                        save = r - 1
                        possible = ''
                        possibleEnd = ''
                        while (r >= l and s[r] == s[l]):
                            possible += s[r]
                            possibleEnd += s[l]
                            r -= 1
                            l += 1
                        if (r > l):
                            l = i
                            r = save

                        else:
                            possibleEnd = possibleEnd[::-1]
                            if (l - r == 1):
                                possible += possibleEnd
                            else:
                                possible += possibleEnd[1:]
                            if len(possible) > len(answer):
                                answer = possible
        if answer == '':
            return s[0]
        
        return answer
        

solution = Solution().longestPalindrome

print (solution("aaabaaaa"))
