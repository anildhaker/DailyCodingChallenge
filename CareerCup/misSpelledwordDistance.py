# Given a dictionary of words &
# a miss-spelled input,
# write a function which will find 3 words from the dictionary which are
# closest (by difference of 1-character) to the given input. 

# eg - dict = {vil, sit, flick, pat, pluck, sat, vat},
# input = vit,
# ans = {sit, vil, vat}


def compute_distance(p, q):
  assert len(p) == len(q)

  dist = 0
  for k in range(len(p)):
    if (p[k] != q[k]):
      dist += 1
  return dist

def close_words(input, dictionary):
  result = []
  for word in dictionary:
    if len(word) == len(input):
      if compute_distance(input, word) == 1:
        result.append(word)
      if len(result) == 3:
        break

  