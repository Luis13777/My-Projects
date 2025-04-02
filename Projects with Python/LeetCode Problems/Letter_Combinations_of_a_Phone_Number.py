class Solution:
    def letterCombinations(self, digits):

        if len(digits) == 0:
            return []

        codes = {
            "0": [" "],
            "1": [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        contador = [[0, len(codes[digit])] for digit in digits]

        ans = []

        while True:
            resposta = ""
            for i in range(len(digits)):
                resposta = resposta + codes[digits[i]][contador[i][0]]

            ans.append(resposta)
                
            j = 0
            contador[j][0] += 1
            while True:
                if contador[j][0] == contador[j][1] and j + 1 < len(contador):
                    contador[j + 1][0] += 1
                    contador[j][0] = 0
                    j += 1
                elif contador[j][0] == contador[j][1] and j + 1 == len(contador):
                    return ans
                else:
                    break



solucao = Solution()
print(solucao.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]