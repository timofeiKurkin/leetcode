package main

func longestCommonSubsequence(text1, text2 string) int {
	m := len(text1)
	n := len(text2)

	dp := make([][]int, m+1)
	for j := 0; j <= m; j++ {
		dp[j] = make([]int, n+1)
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}

	return dp[m][n]
}
