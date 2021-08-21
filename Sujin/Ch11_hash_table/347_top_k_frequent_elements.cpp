#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

struct compare{
    bool operator()(pair<int, int> &a, pair<int, int> &b){
        return a.second < b.second;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
        unordered_map<int, int> map;
        vector<int> res;
        
        for(int i=0; i<nums.size(); i++){
            map[nums[i]]++;
        }
        for(auto element: map){
            pq.push(make_pair(element.first, element.second));
        }
        for(int i=0; i<k; i++){
            res.push_back((pq.top()).first);
            pq.pop();
            if(pq.empty()) break;
        }
        return res;
    }
};