#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> nums2;
    vector<vector<int>> res;
    vector<int> tmp;
    int ch[22]={0, };
    int size;
    
    void DFS(int idx){
        if(idx==size){
            res.push_back(tmp);
        }
        else{
            for(int i=0; i<size; i++){
                if(ch[nums2[i]+11]==0){
                    ch[nums2[i]+11]=1;
                    tmp.push_back(nums2[i]);
                    DFS(idx+1);
                    ch[nums2[i]+11]=0;
                    tmp.pop_back();
                }
            }
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        nums2.assign(nums.begin(), nums.end());
        size = nums.size();
        
        DFS(0); // 첫번째 인자 : nums벡터의 인덱스, 두번째 인자: ch배열의 인덱스
        
        return res;
    }
};