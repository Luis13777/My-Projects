from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Common = strs[0]
        for i in range (1, len(strs)):
            NewCommon = ''
            Equal = True
            j = 0
            if (Common != ''):     
                while (Equal and j < len(strs[i]) and j < len(Common)):
                    if Common[j] == strs[i][j]:
                        NewCommon += Common[j]
                    else:
                        if Common[0] != strs[i][0]:
                            NewCommon = ''
                        Equal = False
                    j += 1
                Common = NewCommon

        return Common

solution = Solution()

print (solution.longestCommonPrefix(["a","aca","accb","b"]))