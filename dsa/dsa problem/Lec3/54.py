# 54. Spiral Matrix

def spiralmatrix(matrix):
    n = len(matrix)        # number of rows
    m = len(matrix[0])     # number of cols

    totalelems = n * m
    ans = []
    cnt = 0

    # initialize boundaries
    rowstart, rowend = 0, n - 1
    colstart, colend = 0, m - 1

    while cnt < totalelems:
        # 1) Traverse top row → left to right
        for i in range(colstart, colend + 1):
           
                ans.append(matrix[rowstart][i])
                cnt += 1
        rowstart += 1  # shrink top boundary

        # 2) Traverse right col → top to bottom
        for i in range(rowstart, rowend + 1):
          
                ans.append(matrix[i][colend])
                cnt += 1
        colend -= 1  # shrink right boundary

        # 3) Traverse bottom row → right to left
        for i in range(colend, colstart - 1, -1):
        
                ans.append(matrix[rowend][i])
                cnt += 1
        rowend -= 1  # shrink bottom boundary

        # 4) Traverse left col → bottom to top
        for i in range(rowend, rowstart - 1, -1):
          
                ans.append(matrix[i][colstart])
                cnt += 1
        colstart += 1  # shrink left boundary

    return ans
matrix = [
 [1, 2, 3,3],
 [4, 5, 6,4],
  [4, 5, 6,4],
 [7, 8, 9,5]
]
print(spiralmatrix(matrix))

# ye index number hota hai
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)
