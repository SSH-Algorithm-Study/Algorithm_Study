#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <queue>
using namespace std;

struct compare{
    bool operator()(string& a, string& b){
        return a > b; // 사전순 정렬
    }
};

class Solution {
public:
    map<string, priority_queue<string, vector<string>, compare>> m;
    vector<string> res; // 결과를 반환할 벡터 res
    
    void DFS(string s){
        while(!m[s].empty()){
            string next = m[s].top();
            m[s].pop();
            DFS(next);
        }
        res.insert(res.begin(), s);
        cout<<s<<endl;
    }
    
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        
        for(int i=0; i<tickets.size(); i++){
            m[tickets[i][0]].push(tickets[i][1]);
        }
        DFS("JFK");
        
        return res;
    }
};