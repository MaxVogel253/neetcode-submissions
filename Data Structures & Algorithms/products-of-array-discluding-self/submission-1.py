class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # The len function is used  to determine the built in length of how many
        #items in an object.

        answer = [1] * n
        #This creates as many lists as there are items in num

        left_product = 1
        #This starts the left position in the array, allowing us to move it up

        for i in range(n):

            answer[i] = left_product

            left_product *= nums[i]

        right_product = 1
        
        for i in range(n - 1, -1,-1):


            answer[i] *= right_product


            right_product *= nums[i]

            
            
        return answer
        #This returns the answer of our finalized product


    

        
       
