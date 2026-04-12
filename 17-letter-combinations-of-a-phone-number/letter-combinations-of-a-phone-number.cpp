#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits.empty()) return {};
        
        vector<string> map = {
            "", "", "abc", "def", "ghi", "jkl",
            "mno", "pqrs", "tuv", "wxyz"
        };
        
        vector<string> result;
        result.push_back("");
        
        for(char digit : digits) {
            vector<string> temp;
            string letters = map[digit - '0'];
            
            for(string s : result) {
                for(char c : letters) {
                    temp.push_back(s + c);
                }
            }
            
            result = temp;
        }
        
        return result;
    }
};