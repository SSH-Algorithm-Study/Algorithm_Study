#include <iostream>
#include <cmath>
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    struct cmp{
        bool operator()(vector<int>&a, vector<int>&b){
            double res1 = hypot(a[0], a[1]);
            double res2 = hypot(b[0], b[1]);
            
            return res1 > res2;
        }
    };
    
    vector<vector<int> > kClosest(vector<vector<int> >& points, int k) {
        priority_queue<vector<int>, vector<vector<int> >, cmp> pq;
        
        for(int i=0; i<points.size(); i++){
            pq.push(points[i]);
        }
        
        vector<vector<int> > res;
        for(int i=0; i<k; i++){
            res.push_back(pq.top());
            pq.pop();
        }
        
        return res;
    }
};