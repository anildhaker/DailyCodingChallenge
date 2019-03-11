# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

class Solution:
    def findRestaurant(self, list1, list2):
        
        res = []
        min_sum = float('inf')
        for i,v in enumerate(list1):
            if v in list2:
                j = list2.index(v)
                if i+j <= min_sum:
                    min_sum = i+j
                    res.append(v)
        return res   
                
                