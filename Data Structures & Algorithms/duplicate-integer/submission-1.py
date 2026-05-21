
class Solution:
    def hasDuplicate(self, nums):



        seen = set()

        # Creates a value 


        for num in nums:
            #creates a lucid value that iterates through nums
            if num in seen:
                #This checks that if there are multiple values in the set
                return True
                #returns true
            seen.add(num)
            #This adds the value to set()

        return False
        #Returns false if untrue
