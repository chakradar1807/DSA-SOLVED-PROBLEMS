#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int count = 0;
    
    void solve(int row, int n, vector<int>& cols, vector<int>& d1, vector<int>& d2) {
        if(row == n) {
            count++;
            return;
        }
        
        for(int col = 0; col < n; col++) {
            if(cols[col] || d1[row + col] || d2[row - col + n - 1]) continue;
            
            cols[col] = d1[row + col] = d2[row - col + n - 1] = 1;
            solve(row + 1, n, cols, d1, d2);
            cols[col] = d1[row + col] = d2[row - col + n - 1] = 0;
        }
    }
    
    int totalNQueens(int n) {
        vector<int> cols(n, 0), d1(2*n, 0), d2(2*n, 0);
        solve(0, n, cols, d1, d2);
        return count;
    }
};