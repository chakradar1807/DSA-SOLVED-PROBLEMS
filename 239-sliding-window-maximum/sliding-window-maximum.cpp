class Solution {
 //OPTIMISED
 public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    //base case
    if(k == 1)  return nums;
    vector<int> ans;
    int maxi = INT_MIN, n = nums.size();
    for(int i = 0;i < k; i++){
        maxi = max(maxi, nums[i]);
    }
    ans.push_back(maxi);
    //sliding the window now 
    for(int r = 1; r <= n - k; r++){
        //incoming element becomes the nex maximum
        if(nums[r + k - 1] > maxi){
            maxi = nums[r + k - 1];
            ans.push_back(maxi);
            continue;
        }
        //outgoing element is equal to maxim but another occurence of the same maximum can still exist in the window
        if(nums[r] == maxi) {
            ans.push_back(maxi);
            continue;
        } 
        //the prev maximumhas left the window, recalc max of the new window
        if(nums[r - 1] == maxi) {
            maxi = INT_MIN;
            for(int j = 0; j < k; j++) {
                maxi = max(maxi, nums[r+j]);
            }
            ans.push_back(maxi);
        } else {//curr max iss still inside the  window
            ans.push_back(maxi);
        }
    }
        return ans;
  }
};

    //BRUTE FORCE APPROACH !
// public: 
//     vector<int> maxSlidingWindow(vector<int>& nums, int k) {
//         vector<int> ans;
//         for(int r = k - 1; r < nums.size(); r++) {
//             int maxi = INT_MIN;
//             int l = r - k + 1;
//             int  x = *max_element(nums.begin() + l, nums.begin()+ r + 1);
//             maxi = max(maxi, x);
//             ans.push_back(maxi);
//         }
//         return ans;
//     }