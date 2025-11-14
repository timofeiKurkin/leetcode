n = int(input())
nums = list(map(int, input().split()))

MOD = 10**9 + 7

pow2 = [1] * (n + 1)
for i in range(1, n + 1):
    pow2[i] = (pow2[i - 1] * 2) % MOD

F = [0] * (n + 1)
F[0] = 1
last = {}

for i in range(1, n + 1):
    x = nums[i - 1]
    if x in last:
        j = last[x]
        term = (F[j - 1] * pow2[i - j - 1]) % MOD
        F[i] = (2 * F[i - 1] - term) % MOD
    else:
        F[i] = (2 * F[i - 1]) % MOD
    last[x] = i

ans = (F[n] - 1) % MOD
if ans < 0:
    ans += MOD

print(ans)
