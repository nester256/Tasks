def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * (N + 2) for _ in range(M)]
    for i in range(M):
        dp[i][0] = dp[i][-1] = float('inf')
        for j in range(1, N + 1):
            dp[i][j] = matrix[i][j - 1]
    for i in range(1, M):
        for j in range(1, N + 1):
            dp[i][j] = matrix[i][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
    return min(dp[-1])