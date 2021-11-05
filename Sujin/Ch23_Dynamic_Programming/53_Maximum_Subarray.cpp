class Solution {
public:
    int dp[100001]={0, };
    
    int maxSubArray(vector<int>& nums) {
        dp[0]=nums[0];
        int max_sum = dp[0];
        
        for(int i=1; i<nums.size(); i++){
            dp[i] = max(nums[i], dp[i-1]+nums[i]);
            max_sum = max(max_sum, dp[i]);
        }
        
        return max_sum;
        
    }
};​