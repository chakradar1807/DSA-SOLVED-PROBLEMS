class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        
        vector<vector<int>> pos(26);

        // store positions of characters
        for(int i = 0; i < s.size(); i++){
            pos[s[i] - 'a'].push_back(i);
        }

        int count = 0;

        for(string &word : words){
            
            int prev = -1;
            bool found = true;

            for(char c : word){
                auto &vec = pos[c - 'a'];

                auto it = upper_bound(vec.begin(), vec.end(), prev);

                if(it == vec.end()){
                    found = false;
                    break;
                }

                prev = *it;
            }

            if(found) count++;
        }

        return count;
    }
};