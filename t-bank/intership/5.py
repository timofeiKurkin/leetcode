n, k = map(int, input().split())  # (1 <= n,k <= 100)

MOD = 10**9 + 7

# dp = [0] * (n + 1)
# dp[0] = 1

# for i in range(1, n + 1):
#     for _ in range(k):
#         for w in range(i, n + 1):
#             dp[w] += dp[w - i]
#             if dp[w] >= MOD:
#                 dp[w] -= 1

# print(dp[n] % MOD)


C = [0] * (n + 1)
C[0] = 1
for t in range(1, n + 1):
    C[t] = C[t - 1] * (t + k - 1) % MOD
    C[t] = C[t] * pow(t, MOD - 2, MOD) % MOD

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    new_dp = dp[:]
    for t in range(1, n // i + 1):
        coef = C[t]
        for j in range(i * t, n + 1):
            new_dp[j] = (new_dp[j] + dp[j - i * t] * coef) % MOD
    dp = new_dp

print(dp[n] % MOD)
