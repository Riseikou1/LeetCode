from typing import List
from collections import defaultdict

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temuujin = defaultdict(list)
        for s in strs :
            key = ''.join(sorted(s))
            temuujin[key].append(s)
        
        return list(temuujin.values())
    
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temuujin = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s :
                count[ord(c) - ord('a')] += 1
            temuujin[tuple(count)].append(s)
        
        return list(temuujin.values())


if __name__ == "__main__":

    input =  ["eat","tea","tan","ate","nat","bat"]

    solu1 = Solution1()
    output1 = solu1.groupAnagrams(input)
    print(output1)

    solu2 = Solution2()
    output2 = solu2.groupAnagrams(input)
    print(output2)

