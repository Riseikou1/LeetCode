from typing import List

# Brute Force ---  Time complexity : O(n^2) , Space complexity : O(1)
class Solution1:  
    def trap(self, height: List[int]) -> int:

        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
                
            res += min(leftMax, rightMax) - height[i]
        return res
        
        
# Prefix & Suffix Arrays  ---  Time Complexity : O(n) , Space complexity : O(n)
class Solution2: 
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left = [0] * n
        right = [0] * n
        res = 0

        left[0] = height[0]    # Fill left max
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        right[-1] = height[-1]   # Fill right max
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        for i in range(n):   # Calculate trapped water
            water = min(left[i], right[i]) - height[i]
            if water > 0:
                res += water

        return res


class Solution2:
    def trap(self, height: List[int]) -> int:

        vol = 0

        for i in range(len(height)):
            if i < len(height)-1 and height[i+1] >= height[i]:
                continue
            if i < len(height)-1 and height[i+1] < height[i]:
                tmp = 0
                r = i + 1
                while height[r] < height[i] and r < len(height)-1:
                    tmp += (height[i] - height[r])
                    r += 1
                vol += tmp

        return vol        


if __name__ == "__main__":

    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    sol1 = Solution1()
    print(sol1.trap(height))

    sol2 = Solution2()
    print(sol2.trap(height))

