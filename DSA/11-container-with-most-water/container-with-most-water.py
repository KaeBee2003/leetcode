class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        v = min(height[i], height[j])*(j-i)
        
        while i<j:
            
            if min(height[i], height[j]) == height[i]:
                i += 1
            else:
                j -= 1
            
            if min(height[i], height[j])*(j-i) > v:
                v = min(height[i], height[j])*(j-i)

        return v