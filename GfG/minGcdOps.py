# minimum gcd operations to make all array elements 1.

# approach --> if 1 already present => n - count of 1s.
# else : find array of min length with gcd 1 ==> n + len(subarray which has gcd 1) -1

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, b)

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
  if 1 in arr:
    return (len(arr) - one_count(arr))

  else:
    for i in range(len(arr)):
      for j in range(i + 1, len(arr)):
        
    