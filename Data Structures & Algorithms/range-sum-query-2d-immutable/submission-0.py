class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefmatrix = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        self.matrix = matrix
        
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.prefmatrix[i][j] = (self.matrix[i-1][j-1]+
                                        self.prefmatrix[i-1][j]+
                                        self.prefmatrix[i][j-1]-
                                        self.prefmatrix[i-1][j-1])
                                        
                                        

#formula for prefmatrix - matrix[i][j] + prefix[i-1][j]+ prefix[i][j-1] prefix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = (self.prefmatrix[row2+1][col2+1]
                - self.prefmatrix[row1][col2+1]
                - self.prefmatrix[row2+1][col1]
                + self.prefmatrix[row1][col1])
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)