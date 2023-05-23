class Solution:
    def isValid(self, s):
        stack=[]
        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char==']' and stack[-1] !='[' :
                    return False   
                elif char=='}' and stack[-1] !='{' :
                    return False   
                elif char==')' and stack[-1] !='(' :
                    return False  
                else:
                    stack.pop()
        return not stack   
    
solution = Solution()
print(solution.isValid("[][]())"))