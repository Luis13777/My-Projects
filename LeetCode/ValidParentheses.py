class Solution:
    def isValid(self, s: str) -> bool:
        stack = ''
        for i in range (len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack += s[i]
            else:
                if (len(stack)==0):
                    return False
                if s[i] == '}' and stack[-1] != '{':
                    return False
                if s[i] == ']' and stack[-1] != '[':
                    return False
                if s[i] == ')' and stack[-1] != '(':
                    return False
                
                stack = stack[:-1:]

        if stack == '':
            return True
        return False
    
solution = Solution()
print(solution.isValid("[][]())"))