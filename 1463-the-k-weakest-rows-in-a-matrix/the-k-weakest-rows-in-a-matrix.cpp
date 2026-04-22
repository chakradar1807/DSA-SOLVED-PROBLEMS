class Solution {
public:
    int countSoldiers(vector<int>& row) {
        return count(row.begin(), row.end(), 1);
    }

    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<pair<int, int>> arr;

        for (int i = 0; i < mat.size(); i++) {
            int soldiers = countSoldiers(mat[i]);
            arr.push_back({soldiers, i});
        }

        sort(arr.begin(), arr.end());

        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(arr[i].second);
        }

        return result;
    }
};