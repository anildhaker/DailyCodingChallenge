# Given n non-negative integers a1, a2, ..., an , where each represents a point at
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line
# i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
# container, such that the container contains the most water.

def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height)-1 
        
        area = 0 
        while i < j :
            area = max(area,(j-i)*min(height[i],height[j]))
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area