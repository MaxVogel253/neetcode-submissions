class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        #Saves time by automatically checking if the word lengths are not equal.

        count = {}
        #This creates a hashmap

        for c in s:
            #Iterates through s
            count[c] = count.get(c, 0) + 1
        
        for c in t: 
            #Iterates through t
            count[c] = count.get(c, 0) - 1

        for val in count.values():
            if val != 0:
                return False

        
        return True
                
        
           
            


    

        
