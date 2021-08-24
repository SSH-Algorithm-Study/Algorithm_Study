#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> res;
    vector<int> tmp;
    int ch[21]={0, };
    int nn, kk;
    
    void DFS(int s, int idx){
        if(idx==kk){ // 배열의 인덱스가 0~idx-1까지 다 찼을 때
            for(int i=0; i<idx; i++){
                tmp.push_back(ch[i]);
            }
            res.push_back(tmp);
            tmp.clear();
        }
        else{
            for(int i=s; i<=nn; i++){
                ch[idx]=i;
                DFS(i+1, idx+1);
            }
        }
    }
    
    vector<vector<int>> combine(int n, int k) {
        nn = n;
        kk = k;
        DFS(1, 0); // 첫번째: 시작하는 숫자, 두번째: 시작하는 배열 인덱스
        
        return res;
    }
};