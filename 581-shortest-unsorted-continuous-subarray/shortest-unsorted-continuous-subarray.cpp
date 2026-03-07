class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        
        int n = nums.size();
        int left = -1, right = -1;

        // find first violation from left
        for(int i = 0; i < n-1; i++){
            if(nums[i] > nums[i+1]){
                left = i;
                break;
            }
        }

        if(left == -1) return 0; // already sorted

        // find first violation from right
        for(int i = n-1; i > 0; i--){
            if(nums[i] < nums[i-1]){
                right = i;
                break;
            }
        }

        int subMin = INT_MAX, subMax = INT_MIN;

        for(int i = left; i <= right; i++){
            subMin = min(subMin, nums[i]);
            subMax = max(subMax, nums[i]);
        }

        while(left > 0 && nums[left-1] > subMin)
            left--;

        while(right < n-1 && nums[right+1] < subMax)
            right++;

        return right - left + 1;
    }
};