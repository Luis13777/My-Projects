# . can be any string or char
# * can be 0 or more times

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        j = 0
        i = 0
        sizeS = len(s)
        sizeP = len(p)
        p += '       '
        s += '       '
        while (not(i>=sizeS and j>=sizeP)):
            if (i<sizeS):
                if (p[j] != '*' and p[j] != '.'):
                    if (s[i] == p[j]):
                        j += 1
                        i += 1
                    else:
                        if (p[j+1]!='*'):
                            return False
                        GoAhead = True
                        j -= 1
                        while(GoAhead):
                            j+=2
                            if (p[j+1] != s[i] and p[j+2] != '*'):
                                return False
                            if (p[j+1] == s[i]):
                                j+=2
                                i += 1
                                GoAhead = False


                        if not (p[j+1] == '*' and p[j+2] == s[i]):
                            return False
                        else:
                            j += 3
                            i += 1
                else:
                    if p[j] == '*':
                        if p[j-1] != p[j+1]:
                            while (s[i-1] == s[i]):
                                i += 1
                            j += 1
                        else:
                            # if p[j+2] != '*' and p[j+2] != p[j+1]:
                            #     if s [i] == p[j-1]:
                            #         while (s[i] == s[i-1]):
                            #             i += 1
                            #         i += 1
                            #         j += 2
                            #     else:
                            #         j += 2
                            # else:
                            CasesInP = 1 
                            while (p[j] == s [i-1] or p[j] == '*'):
                                if (p[j] != '*'):
                                    CasesInP += 1
                                else:
                                    CasesInP -= 1
                                j += 1
                            CasesInS = 1
                            while s[i] == s[i-1]:
                                i += 1
                                CasesInS += 1
                            if (s[i-1] != s[i-2]):
                                i += 1
                            if CasesInS < CasesInP:
                                return False
                            
            else:
                if(p[j] != '*'):
                    j+=1
                    while j<sizeP:
                        if (p[j] != '*'):
                            return False
                        j = j + 2
                else:
                    while j<sizeP:
                        if (p[j] != '*'):
                            return False
                        j = j + 2

        if (j<sizeP):
            return False                       

        return True            


solution = Solution()
print(solution.isMatch("abca", "abc*x*a*v*a"))