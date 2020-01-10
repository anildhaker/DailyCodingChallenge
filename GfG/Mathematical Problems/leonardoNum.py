# leonardo num => l(n) = l(n-1) + l(n-2) + 1

# recursive solution. 
def leonardo(n):
  if n == 0 or n == 1:
    return 1
  else:
    return leonardo(n - 1) + leonardo(n - 2) + 1


def leonardoDp(n):
  dp = []
  dp.append(1)
  dp.append(1)

  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2] + 1)
    
  return dp[n]

print(leonardo(3))
print(leonardoDp(3))


 