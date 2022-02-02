class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_cost=prices[0];
        int profit=0;
        
        for(int i=1; i<prices.size(); i++){
            buy_cost=min(buy_cost, prices[i]);
            if(prices[i]>buy_cost){
                profit+=(prices[i]-buy_cost);
                buy_cost=prices[i];
            }
        }
        return profit;
    }
};
