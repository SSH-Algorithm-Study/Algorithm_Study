#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_cost = prices[0];
        int profit = 0;
        
        for(int i=1; i<prices.size(); i++){
            profit = max(profit, prices[i]-buy_cost); // sliding window 기법
            if(prices[i]<buy_cost) buy_cost = prices[i];
        }
        return profit;
    }
};