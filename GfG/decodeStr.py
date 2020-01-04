# find possible num of decodings of num.
# eg 121 -- "ABA", "AU", "LA"

# Approach --
# 1. if last digit is non-zero -- recur for remaining n-1 add count + 1
# 2. if last two digits forms a valid char combo then recur for n-2 add count +=1 


def numDecodings(s):
  n = len(s)
  count = [0] * (n + 1)
  
  count[0] = 1  # for empty string
  count[1] = 1  # for 1 digit present
  
  for i in range(2, n + 1):
    count[i] = 0
    if s[i - 1] > '0':
      count[i] = count[i - 1]
      
    if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
      count[i] += count[i - 2]

  return count[n]
  
s = ['1', '2', '3', '4']
p = ['1','2','2','1']
print(numDecodings(p))
      