class Solution:
    def romanToInt(self, s: str) -> int:
        switcher = {
        'I': "1",
        'V': "5",
        'X': "10",
        'L': "50",
        'C': "100",
        'D': "500",
        'M': "1000"
        }
        numero = 0
        numeros = [0]*(len(s) + 1)
        for i in range (len(s)):
            numeros[i] = int(switcher[s[i]])
        i = 0
        while (i<len(s)):

            if (numeros[i]>=numeros[i+1]):
                numero += numeros[i]
            else:
                numero += numeros[i + 1] - numeros[i]
                i += 1
            i += 1

        print (numeros)
        print (numero)
        return numero

sol = Solution()

sol.romanToInt("MCMXCIV")
sol.romanToInt("MCMXCI")
sol.romanToInt("MCMXC")