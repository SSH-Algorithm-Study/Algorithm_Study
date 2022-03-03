class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_cost = prices[0];
        priority_queue<int> pq;
        pq.push(0);
        
        for(int i=1; i<prices.size(); i++){
            buy_cost = min(buy_cost, prices[i]);
            pq.push(prices[i]-buy_cost);
        }
        
        return pq.top();
    }
};
