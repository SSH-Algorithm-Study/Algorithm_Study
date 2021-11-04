class Solution {
public:
    int dp[31]={0, };
    
    int fib(int n) {
        if(dp[n]) return dp[n];
        
        if(n==0) return dp[0]=0;
        if(n==1) return dp[1]=1;
        
        return dp[n]=fib(n-1)+fib(n-2);
    }
};