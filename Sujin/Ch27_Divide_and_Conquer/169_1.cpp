class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> um;
        for(int i=0; i<nums.size(); i++) um[nums[i]]++;
        int key=0, val=0;
        for(auto a: um){
            if(a.second>val){ key=a.first; val=a.second; }
        }
        return key;
    }
};
