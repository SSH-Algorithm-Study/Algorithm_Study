class Solution {
public:
    int dp[101]={0, };
    
    int rob(vector<int>& nums) {
        if(nums.size()==1) return nums[0]; // 예외처리1
        if(nums.size()==2) return max(nums[0], nums[1]); // 예외처리2
        
        dp[0] = nums[0];
        dp[1] = nums[1];
        dp[2] = dp[0]+nums[2];
        
        int max_num = max(dp[1], dp[2]); // 임시 max_num 계산
        
        for(int i=3; i<nums.size(); i++){
            dp[i] = max(dp[i-3], dp[i-2]) + nums[i];
            max_num = max(max_num, dp[i]);
        }
        
        return max_num;
    }
};