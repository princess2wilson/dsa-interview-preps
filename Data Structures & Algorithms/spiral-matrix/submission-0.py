class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:

            #Add first row to result
            res+=(matrix.pop(0))
            
            #append last element of all lists to the result
            if matrix and matrix[0]:
                for arr in matrix:
                    res.append(arr.pop())

            #add the reverse of the last row
            if matrix:
                last = matrix.pop()
                reverse_last = last[::-1]

                res+=reverse_last

            #add the first index of each remaining row
            if matrix and matrix[0]:
                for x in matrix[::-1]:
                    res.append(x.pop(0))
        return res






