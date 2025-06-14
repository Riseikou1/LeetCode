#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution1{
public :
    bool isAnagram(string s, string t){ // it is the slowest shit.

        if(s.length() != t.length()) return false;

        unordered_map<int,int> sCount, tCount;

        for(int i=0;i<s.length();i++){
            sCount[s[i]] = 1 + sCount[s[i]];
            tCount[t[i]] = 1 + tCount[t[i]];
        }
        return sCount == tCount;
   }   
};

class Solution2 {   /// this is the fastest shit among here.
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        vector<int> count(26, 0);

        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int c : count) {
            if (c != 0) return false;
        }

        return true;
    }
};

class Solution3{
    bool isAnagram(string s, string t){
        if(s.length() != t.length()) return false;
        unordered_map<char,int> temuujin;

        for(char ch : s){
            temuujin[ch] += 1;
        }

        for(char ch : t){
            if(temuujin[ch] == 0) return false;
            temuujin[ch] -= 1;
        }
        return true;
    }
};

class Solution4 {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, int> count;

        for (int i = 0; i < s.length(); i++) {
            count[s[i]]++;   //
            count[t[i]]--;   // if same letter happens to come from 2nd array, decrease its frequency.
        }

        for (auto& [ch, freq] : count) {
            if (freq != 0) return false;  // of course after decreasing and increasing according to what is in the lists, frequency must be 0 where it is valid anagram.
        }

        return true;
    }
};


int main(){

    Solution1 sol1;

    string string1 = "anagram"; 
    string string2 = "naagram";

    cout << (sol1.isAnagram(string1,string2) ? "True" : "False") << endl;

    return 0;   
}