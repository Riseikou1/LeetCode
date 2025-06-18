from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs :
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

if __name__ == "__main__":

    sol = Solution()
    list = ["neet","code","love","you"]

    result = sol.encode(list)
    print("Result of encoder : ", result)

    output = sol.decode(result)
    print("Result of decoder : ", output)

