# Every 3-rd Fibonacci number is a multiple of 2
# Every 4-th Fibonacci number is a multiple of 3
# Every 5-th Fibonacci number is a multiple of 5
# Every 6-th Fibonacci number is a multiple of 8

Max = 100

arr = [0] * Max

index_2 = [0]*Max
index_3 = [0]*Max
index_5 = [0]*Max
index_8 = [0]*Max

arr[0] = 0
arr[1] = 1

for i in range(2, Max):
  arr[i] = arr[i - 1] + arr[i - 2]

# print(arr)
# print()
  
c2 = 0
c3 = 0
c5 = 0
c8 = 0 

for i in range(Max):
  if arr[i] % 2 == 0:
    index_2[c2] = i
    c2 += 1

  if arr[i] % 3 == 0:
    index_3[c3] = i
    c3 += 1
  
  if arr[i] % 5 == 0:
    index_5[c5] = i
    c5 += 1
  
  if arr[i] % 8 == 0:
    index_8[c8] = i
    c8 += 1


for i in range(c2):
  print(index_2[i], end=" ")

print()

for i in range(c3):
  print(index_3[i], end=" ")
print()

for i in range(c5):
  print(index_5[i], end=" ")
print()

for i in range(c8):
  print(index_8[i], end=" ")
print()
  