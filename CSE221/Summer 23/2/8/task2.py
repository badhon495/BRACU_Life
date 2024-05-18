def count_ways(n, dp):
    if dp[n] != -1:
        return dp[n]
    if n == 0 or n == 1:
        dp[n] = 1
    else:
        dp[n] = count_ways(n - 1, dp) + count_ways(n - 2, dp)
    return dp[n]

with open('input2_4.txt', 'r') as inp:
    with open('output2_4.txt', 'w') as out:
      n = int(inp.readline())
      dp = [-1] * (n + 1)
      print(count_ways(n, dp),file=out)