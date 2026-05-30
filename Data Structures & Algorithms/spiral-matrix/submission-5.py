class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res+=(matrix.pop(0))

            if matrix and matrix[0]:
                for x in matrix:
                    res.append(x.pop())
            
            if matrix:
                arr = matrix.pop()[::-1]
                for x in arr:
                    res.append(x)

            if matrix and matrix[0]:
                for x in matrix[::-1]:
                    res.append(x.pop(0))
        return res
                    


            
            
            #[[4,5]
            
                
            
            

            
