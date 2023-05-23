class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        numero = ""
        length = len(s)
        s += ' '
        isOver = False
        Negative = False
        while (i<length and not isOver):
            if s[i]=='-' and s[i+1].isdigit():
                Negative = True
                i += 1 
            if s[i]=='+' and s[i+1].isdigit():
                i += 1 
            if s[i]!=' ' and s[i].isdigit():
                numero += s[i]
                if not s[i+1].isdigit():
                    isOver = True
            elif s[i]!=' ':
                isOver = True

            i += 1                
        
        if (numero == ''):
            return 0
        if (Negative):
            numero = -int(numero)
            if numero >= -2**31:
                return numero
            return -2**31
        numero = int(numero)
        if numero <= 2**31 - 1:
            return numero
        return 2**31 - 1
            

solution = Solution()

print(solution.myAtoi(" +1"))
