class Solution { // Author:- KaiHiwatari 
public:
    int search(vector<int>& nums, int target) {
        for(int i=0;i<nums.size();i++){
            if(nums[i] == target){ // if i in array of nums == target then
                return(i); // return i returns the index of i
            }
        }
        return -1; // return  -1 when target is not found in the list  
    }
};