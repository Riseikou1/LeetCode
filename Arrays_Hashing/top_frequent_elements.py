from typing import List
import heapq

class Solution1:   #  Using heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        temuujin = {}
        heap = []
        
        for num in nums : 
            temuujin[num] = temuujin.get(num,0) + 1

        for key, val in temuujin.items():
            if len(heap) < k :
                heapq.heappush(heap,(val,key))
            else :
                heapq.heappush(heap,(val,key))
                heapq.heappop(heap)   # instantly popping for keeping the heap size same as k and only keeping max values.(heap is min by default soo,pop deletes the min shit)
        
        return [h[1] for h in heap]
    

class Solution2:  # Using Bucket Sort    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temuujin = {}
        freq = [[] for _ in range(len(nums)+1)]
        
        for num in nums : 
            temuujin[num] = temuujin.get(num,0) + 1

        for key, val in temuujin.items():
            freq[val].append(key)
        
        res = []

        for i in range(len(freq)-1 , -1 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k : 
                    return res


if __name__ == "__main__":

    nums = [1,2,2,3,3,3]
    k = 2

    solu1 = Solution1()
    outpu1 = solu1.topKFrequent(nums,k)  # returns k number of largest frequency elements.
    print(outpu1)


    solu2 = Solution2()
    outpu2 = solu2.topKFrequent(nums,k) 
    print(outpu2)

