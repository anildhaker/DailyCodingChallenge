# minimum gcd operations to make all array elements 1.

# approach --> if 1 already present => n - count of 1s.
# else : find array of min length with gcd 1 ==> n + len(subarray which has gcd 1) -1

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)

def gcd_array(arr):
  res = 1
  for i in range(len(arr)):
    res = gcd(res, arr[i])
  return res

def one_count(arr):
  count = 0
  for i in range(len(arr)):
    if arr[i] == 1:
      count += 1
  return count  

def countOps(arr):
  n = len(arr)
  if one_count(arr) != 0:
    return n - one_count(arr)

  minimum = +2147483647
  for i in range(n):
    g = arr[i]
    for j in range(i + 1, n):
      g = gcd(g, arr[j])
      if g == 1:
        minimum = min(minimum, j - i)
        break
  if (minimum == +2147483647): 
      return -1
  else: 
      return n + minimum - 1

    
arr = [2,4,3,9]
print(countOps(arr))    