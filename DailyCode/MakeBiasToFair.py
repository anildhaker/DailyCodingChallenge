# Makeafaircoin from a biasedc oin

# You are given a function foo() that represents a biased coin.
# When foo() is called, it returns 0 with 60% probability,
# and 1 with 40% probability. Write a new function that returns 0 and 1 with 50 Percent


def foo():   # already given function
  pass

def my_func():
  val_1 = foo()
  val_2 = foo()

  if val_1 == 0 and val_2 == 1:
    return 0

  if val_1 == 1 and val_2 == 0:
    return 1

  return my_func()







