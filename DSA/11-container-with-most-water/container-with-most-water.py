class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        max_vol = min(height[i], height[j])*(j-i)
        
        while i<j:

            if min(height[i], height[j]) == height[i]:
                i += 1
            else:
                j -= 1
            
            curr_vol = min(height[i], height[j])*(j-i)
            if curr_vol > max_vol:
                max_vol = curr_vol

        return max_vol