#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

class Solution1 {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string,vector<string>> ans;

        for(string& s : strs){
            string key = s;
            sort(key.begin(),key.end());
            ans[key].push_back(s);
        }

        vector<vector<string>> result;
        for(auto& entry : ans){
            result.push_back(entry.second);
        }

        return result;
    }
};


class Solution2{
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string,vector<string>> temuujin;

        for(string& s : strs){
            vector<int> count(26,0);
            for(char ch : s){
                count[ch - 'a'] += 1;
            }
            string key;
            for(int num : count){
                key += to_string(num) + "#";
            }
            temuujin[key].push_back(s);
        }

        vector<vector<string>> result;
        for(auto& entry : temuujin){
            result.push_back(move(entry.second));
        }
        return result;
    }
};

int main(){

    Solution1 solu;

    vector<string> input = {"eat","tea","tan","ate","nat","bat"};

    vector<vector<string>> result = solu.groupAnagrams(input);

    // Print the result
    for (const auto& group : result) {
        for (const auto& word : group) {
            cout <<word << " ";
        }
        cout << endl;
    }

    return 0;
}