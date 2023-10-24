class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        MAX = 0
        for position in range(len(s)):
            lengthOfSubArrayLeft = 0
            lengthOfSubArrayRight = 0

            # left
            changes = 0
            i = 0
            while (changes < k and position - i >= 0):
                if s[position - i] != s[position]:
                    changes += 1
                lengthOfSubArrayLeft += 1
                i += 1
            while position - i >= 0 and s[position - i] == s[position]:
                lengthOfSubArrayLeft += 1
                i += 1

            if position - i < 0 and changes < k:
                i = 1
                while (changes < k and position + i < len(s)):
                    if s[position + i] != s[position]:
                        changes += 1
                    lengthOfSubArrayLeft += 1
                    i += 1
                while position + i < len(s) and s[position + i] == s[position]:
                    lengthOfSubArrayLeft += 1
                    i += 1
            
            # right
            changes = 0
            i = 0
            while (changes < k and position + i < len(s)):
                if s[position + i] != s[position]:
                    changes += 1
                lengthOfSubArrayRight += 1
                i += 1
            while position + i < len(s) and s[position + i] == s[position]:
                lengthOfSubArrayRight += 1
                i += 1

            if position + i >= len(s) and changes < k:
                i = 1
                while (changes < k and position - i >= 0):
                    if s[position - i] != s[position]:
                        changes += 1
                    lengthOfSubArrayRight += 1
                    i += 1
                while position - i >= 0 and s[position - i] == s[position]:
                    lengthOfSubArrayRight += 1
                    i += 1

            MAX = max(lengthOfSubArrayRight, lengthOfSubArrayLeft, MAX)
        
        return MAX
    

solution = Solution().characterReplacement

print(solution("BAAAB", 2))