class Solution {
public:
    int jump(vector<int>& nums) {
        
        int j=0; 
        int n=nums.size(),i=0;
        int cm=nums[0];
        int cnt=0;

        while(i<n-1 && j<n-1){
            while(i<=min(n-1,j)){
                cm=max(cm,i+nums[i]);
                i++;
            }

            cnt++;

            if(i>=n-1){
                return cnt;
            }

            j=cm;
            cm=nums[i]+i;
        }

        return cnt;
    }
};