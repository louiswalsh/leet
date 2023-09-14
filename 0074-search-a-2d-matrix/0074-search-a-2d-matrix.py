class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        mLeft, mRight = 0, len(matrix) - 1
        matrixIndex = None

        while mLeft <= mRight:
            guess = (mLeft + mRight) // 2
            print(guess)
            
            if matrix[guess][0] <= target <= matrix[guess][len(matrix[guess]) - 1]:
                matrixIndex = guess
                break

            elif target < matrix[guess][0]:
                print('in smaller matrix')
                mRight = guess - 1

            else: 
                print('in larger matrix')
                mLeft = guess + 1

        if matrixIndex == None:
            return False

        for i in matrix[matrixIndex]:
            if i == target:
                return True

        return False

        