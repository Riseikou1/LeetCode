#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

// Single pass hashmap method.
class Solution{
public :
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int,int> numMap;
        int n = nums.size();
        for(int i=0;i<n;i++){
            int complement = target - nums[i];
            if(numMap.count(complement)){
                return {numMap[complement],i};
            }
            numMap[nums[i]] = i;
        }
        return {};
    }
};

// 2 pass hashmap method.
class Temuujin {
public :
    vector<int> twoSum(vector<int>& nums,int target){
        unordered_map<int,int> numMap;
        int n = nums.size();
        for(int i=0;i<n;i++){
            numMap[nums[i]] = i;
        }
        for(int i=0;i<n;i++){
            int complement = target - nums[i];
            if(numMap[complement]!=i && numMap.count(complement)){
                return {numMap[complement],i};
            }
        }
        return {};
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> result = solution.twoSum(nums, target);

    if (!result.empty()) {
        cout << "Indices: " << result[0] << ", " << result[1] << endl;
    } else {
        cout << "No solution found!" << endl;
    }

    Temuujin temuujin;

    vector<int> temuujin_result = temuujin.twoSum(nums,target);

    cout << "Results from Temuujin : " << result[0] << ", " << result[1] << endl;

    return 0;
}
