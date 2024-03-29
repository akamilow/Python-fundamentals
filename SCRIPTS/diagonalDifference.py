"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9 

The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left
diagonal = 3 + 5 + 9 = 17. Their absolute difference is
|15 — 17| = 2
"""

def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][len(arr)-1-i]
    return abs(sum1-sum2)

print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))