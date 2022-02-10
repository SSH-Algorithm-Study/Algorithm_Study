class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int start_idx=0;
        int n = gas.size(); int sum=0;
        
        int gas_sum = accumulate(gas.begin(), gas.end(), 0);
        int cost_sum = accumulate(cost.begin(), cost.end(), 0);
        if(cost_sum > gas_sum) return -1;
        
        for(int i=0; i<n; i++){
            sum += gas[i]-cost[i];
            if(sum<0){
                start_idx=i+1;
                sum=0;
            }
        }
        return start_idx;
    }
};
