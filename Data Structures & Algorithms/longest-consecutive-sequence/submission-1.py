class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        allnums = set(nums)
        #This creates the hashsetfor the nums, a hashset is used to store random
        #variables, it also does not allow duplicates.



        longestseq = 0
        #This is what we will use to store our answer, and return it later on 

        for num in nums:
            if num - 1 not in nums:
                next_num = num + 1
                length = 1

                

                while next_num in nums:

                    next_num += 1
                    length += 1

                longestseq = max(longestseq, length)

                


        return longestseq


        

    
            



        
