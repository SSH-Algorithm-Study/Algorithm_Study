class Solution {
public:
    int dp[46]={0, };
    
    int climbStairs(int n) {
        if(dp[n]) return dp[n];
        
        if(n==1) return dp[1]=1;
        if(n==2) return dp[2]=2;
        
        return dp[n]=climbStairs(n-1)+climbStairs(n-2);
    }
};