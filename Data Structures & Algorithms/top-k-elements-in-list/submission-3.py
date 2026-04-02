class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])

        counter = {}


        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        for key, cnt in counter.items():
            freq[cnt].append(key)

        result = []

        #[[0], [1,2], [3]]
        
        for reversed_index in range(len(freq)-1, 0, -1):

            for item in freq[reversed_index]:
                result.append(item)
                if len(result) == k:
                    
                    return result
                

                    
        return []

     


