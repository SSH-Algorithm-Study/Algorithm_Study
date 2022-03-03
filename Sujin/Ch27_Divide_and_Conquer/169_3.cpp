class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int val=nums[0]; int cnt=1;
        for(int i=1; i<nums.size(); i++){
            if(cnt==0) val=nums[i];
            
            if(val==nums[i]) cnt++;
            else cnt--;
        }
        return val;
    }
};
