class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        a = len(matrix)
        for i in range((a + 1)//2):
            for j in range(a - 1 - i*2):
                matrix[i+j][a - 1-i], matrix[a-1-i][a-1-i-j], matrix[a - 1-i-j][i], matrix[i][i+j] = matrix[i][i+j], matrix[i+j][a - 1-i], matrix[a-1-i][a-1-i-j], matrix[a - 1-i-j][i]