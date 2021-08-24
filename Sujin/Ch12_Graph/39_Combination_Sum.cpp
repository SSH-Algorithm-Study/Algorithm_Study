#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> res;
    vector<int> tmp;
    vector<int> v;
    int t, size;
    
    void DFS(int idx, int sum){ // idx: 시작해야 할 벡터 인덱스 값, sum : 지금까지의 누적 합
        if(sum==t){
            res.push_back(tmp);
        }
        else if(sum>t){
            return;
        }
        else{
            for(int i=idx; i<size; i++){
                tmp.push_back(v[i]);
                DFS(i, sum+v[i]);
                tmp.pop_back();
            }
        }
        
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        v.assign(candidates.begin(), candidates.end());
        t = target;
        size = candidates.size();
        
        DFS(0, 0);
        
        return res;
    }
};