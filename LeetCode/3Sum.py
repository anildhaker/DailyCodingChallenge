# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d=Counter(nums)
        a, b =set(), set()
        for k in nums:
            d[k]-=1
            for i in a:
                if  d[-(k+i)]>0 :
                    b.add((k,i,-(k+i)))
            a.add(k)
        return list(b)  