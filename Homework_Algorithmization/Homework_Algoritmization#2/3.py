
def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    obstacleGrid[0][0] = 1
    for row in range(1, len(obstacleGrid)):
        obstacleGrid[row][0] = int(obstacleGrid[row][0] == 0 and obstacleGrid[row - 1][0] == 1)
    for col in range(1, len(obstacleGrid[0])):
        obstacleGrid[0][col] = int(obstacleGrid[0][col] == 0 and obstacleGrid[0][col - 1] == 1)
    for row in range(1, len(obstacleGrid)):
        for col in range(1, len(obstacleGrid[0])):
            if obstacleGrid[row][col] == 0:
                obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
            else:
                obstacleGrid[row][col] = 0
    return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
