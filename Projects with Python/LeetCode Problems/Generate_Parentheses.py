class Solution:
    def generateParenthesis(self, n):
        if n == 1:
            return ["()"]
        else:
            previous_case = self.generateParenthesis(n-1)
            ans = []
            size = len(previous_case[0])
            for case in previous_case:
                for i in range(size + 1):
                    for j in range(i, size + 1):
                        ans.append(case[:i] + '(' + case[i:j] + ')' + case[j:])

            return list(set(ans))

solucao = Solution().generateParenthesis(3)

for caso in solucao:
    print(caso)
