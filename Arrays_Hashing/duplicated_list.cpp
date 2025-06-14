#include <iostream>
#include <unordered_map>
#include <set>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution1 {  // brute-force method.
public:
    bool containsDuplicate(vector<int>& nums) {
        int size = nums.size();
        for(int i=0;i<size-1;i++){
            for(int j=i+1;j<size;j++){
                if(nums[i] == nums[j]) return true;
            }
        }
        return false;
    }
};


class Solution2 {  // using set.
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> visited;

        for(int num : nums){
            if(visited.count(num)>0) return true;
            visited.insert(num);
        }
        return false;
    }
};


class Solution2 {  // using hashmap.
    public:
        bool containsDuplicate(vector<int>& nums) {
            unordered_map<int,int> temuujin;
    
            for(int num : nums){
                if(temuujin[num] >= 1) return true;
                temuujin[num] ++ ;
            }   
            return false;
        }
    };


int main(){

    Solution1 solu;

    vector<int> nums = {1,2,4,5,5,6,1,6,2};

    cout << "This shit contains duplicated number : " << (solu.containsDuplicate(nums) ? "True" : "False") << endl;

    return 0;
}