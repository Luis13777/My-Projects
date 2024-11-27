class Solution:
    def topKFrequent(self, nums, k):
        numberOfOccurrences = {}
        freq = [[] for i in range (len(nums)+1)]


        for num in nums:
            if num in numberOfOccurrences:
                numberOfOccurrences[num] += 1
            else:
                numberOfOccurrences[num] = 1

        for n, c in numberOfOccurrences.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res