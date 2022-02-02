class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_cost = prices[0];
        vector<int> dp;
        dp.push_back(0);
        
        for(int i=1; i<prices.size(); i++){
            buy_cost = min(buy_cost, prices[i]);
            dp.push_back(prices[i]-buy_cost);
        }
        sort(dp.begin(), dp.end());
        return *(dp.end()-1);
    }
};
