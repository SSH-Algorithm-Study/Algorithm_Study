#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
using namespace std;

struct compare{
    bool operator()(string &a, string &b){
        return a > b; // 사전 순 정렬
    }
};

class Solution {
public:
    map<string, priority_queue<string, vector<string>, compare>> m;
    vector<string> res;
    
    void DFS(string s){
        if(m[s].empty()){
            res.insert(res.begin(), s);
        }
        else{
            while(!m[s].empty()){
                string tmp = m[s].top();
                m[s].pop();
                DFS(tmp);
            }
            res.insert(res.begin(), s);
        }
    }
    
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for(int i=0; i<tickets.size(); i++){
            m[tickets[i][0]].push(tickets[i][1]);
        }
        
        DFS("JFK");
        return res;
    }
};