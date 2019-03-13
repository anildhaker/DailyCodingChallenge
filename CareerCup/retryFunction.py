# Write a retry function, continue to fetch data until u have exhausted max entries.
# If it fails, continue to retry until retry's have been exhausted.

stream = []
def retryFunc(max_attempt):
  retry = 0
  while (retry < max_attempt):
    if stream:
      retry = 0
    else:
      retry += 1

