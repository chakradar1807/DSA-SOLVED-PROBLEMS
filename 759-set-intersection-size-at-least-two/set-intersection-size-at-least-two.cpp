class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        // Sort by end asc, start desc
        sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) {
            if (a[1] == b[1]) return a[0] > b[0];
            return a[1] < b[1];
        });

        int a = -1, b = -1;  // last two chosen points
        int count = 0;

        for (auto &it : intervals) {
            int start = it[0], end = it[1];

            if (start <= a) {
                // already satisfied
                continue;
            }
            else if (start <= b) {
                // need one more
                count += 1;
                a = b;
                b = end;
            }
            else {
                // need two points
                count += 2;
                a = end - 1;
                b = end;
            }
        }

        return count;
    }
};