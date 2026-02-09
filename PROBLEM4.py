#You are given two arrays a[] and b[], return the Union of both the arrays in any order.
#METHOD 1
class Solution:    
    def findUnion(self, a, b):
        # code here
        return list(set(a) | set(b))

#METHOD 2
class Solution:    
    def findUnion(self, a, b):
        # code here
        result = []
        for x in a:
            if x not in result:
                result.append(x)
        
        for y in b:
            if y not in result:
                result.append(y)
        return result
