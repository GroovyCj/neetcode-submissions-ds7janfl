
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num]  = 1 + counter.get(num, 0)

        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        for key, cnt in counter.items():
            freq[cnt].append(key)

        result = []
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
        return []





      
     


    