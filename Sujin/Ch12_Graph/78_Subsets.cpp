#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> nums2;
    vector<vector<int>> res;
    vector<int> tmp;
    int size;
    
    
    void DFS(int idx){
        if(idx==size){
            res.push_back(tmp);
        }
        else{
            tmp.push_back(nums2[idx]);
            DFS(idx+1);
            tmp.pop_back();
            DFS(idx+1);
        }
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        nums2.assign(nums.begin(), nums.end());
        size = nums.size();
        
        DFS(0);
        return res;
    }
};