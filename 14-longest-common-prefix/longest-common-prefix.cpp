class Solution {
public:
    string prefixProblem(string &prefix, string &str){
        int n = min(prefix.size(), str.size());
        string ans = "";
        for(int i=0; i<n; i++){
            if(prefix[i] != str[i])
                break;
            
            ans += prefix[i];
        }
        return ans;
    }
    string longestCommonPrefix(vector<string>& strs) {
        string prefix=strs[0];
        for(string str:strs)
            prefix = prefixProblem(prefix, str);
        
        return prefix;
    }
};