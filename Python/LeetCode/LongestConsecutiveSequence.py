class Solution:
    def longestConsecutive(self, nums):
        table = set()
        for num in nums:
            table.add(num)

        maxLen = 1
        Len = 1
        cur = table[0]
        for i in table[1::1]:
            if i - cur == 1:
                Len += 1
            else:
                Len = 0
            cur = i
            maxLen = max(Len, maxLen)

        return maxLen
solution = Solution().longestConsecutive
solution([0,3,7,2,5,8,4,6,0,1])
        