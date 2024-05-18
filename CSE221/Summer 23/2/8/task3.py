def minimum_coins(n, x, coins):
    INF = float('inf')
    dp = [INF] * (x+1)
    dp[0] = 0
    for i in range(n):
        for j in range(coins[i], x+1):
            dp[j] = min(dp[j], dp[j-coins[i]]+1)
    return dp[x] if dp[x] != INF else -1

with open('input3_2.txt', 'r') as inp:
    with open('output3_2.txt', 'w') as out:
      n, x = map(int, inp.readline().split())
      coins = list(map(int, inp.readline().split()))
      print(minimum_coins(n, x, coins), file=out)
