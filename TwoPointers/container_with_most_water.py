from typing import List

class Solution1:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i, a in enumerate(heights):
            for j in range(i+1,len(heights)):
                tmp = (j-i) * min(heights[j],a)
                res = max(res,tmp)

        return res


class Solution2:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights)-1

        while l < r :
            tmp = (r-l) * min(heights[l],heights[r])
            res = max(res,tmp)
            if heights[l] > heights[r] :
                r -= 1
            else :
                l += 1

        return res

if __name__ == "__main__":

    height = [1,7,2,5,4,7,3,6]   

    sol1 = Solution1()
    print(sol1.maxArea(height))

    sol2 = Solution2()
    print(sol2.maxArea(height))
