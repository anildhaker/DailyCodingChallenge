# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.


def minCostClimbingStairs(self, cost: List[int]) -> int:
      f1 = f2 = 0
      for x in reversed(cost):
          f1, f2 = x + min(f1, f2), f1
      return min(f1, f2)