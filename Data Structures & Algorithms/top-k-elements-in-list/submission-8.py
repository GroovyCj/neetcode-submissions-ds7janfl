class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input:
            nums -> list of ints
            K -> how many of the top elements we want
                I.e. if K is 3 we want the top 3 of the most frequent elements
        Output:
            List of ints -> This is the most frequent elements up to K
        Assumptions:
            A number can only appear the maximum of N times,
                where N is the length of the array
                if len(array) = 6 the most a element can appear is 6
                [1,1,1,1,1,1]
        Questions:
            How do we keep track of the counts of the elements in an array
                For example 2 elements could appear the same amount of times,
                if the array is len = 6, 2 could appear 3 times and 3 could appear 3 times
                
                We could group the elements by the amount of times they appear
        Approach ideas:
            We need to count the frequency of each element that appears in the List
            After that we can group the elements together by their freq 
            Then starting from the most frequent append them to res list
        """
   
        if len(nums) == 1:
            return nums
        




        count: dict = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq: list = [[] for _ in range(len(nums) + 1) ] # we account for how range starts from 0

        for key, cnt in count.items():
            freq[cnt].append(key)
        

        #[[0],[1],[2],[3, 4]] The list looks something like this now, rough estimate

        res: list = []
        # print(freq)

        for num_list in reversed(freq):
            for item in num_list:
                res.append(item)
                if len(res) == k:
                    return res