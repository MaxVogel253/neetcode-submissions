class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        allnums = set(nums)

        longestseq = 0

        for num in nums:
            if num - 1 not in nums:
                next_num = num + 1 
                length = 1
                while next_num in allnums:
                    length += 1 
                    next_num +=1
                longestseq = max(longestseq, length)

        return longestseq







       
       


            



        
