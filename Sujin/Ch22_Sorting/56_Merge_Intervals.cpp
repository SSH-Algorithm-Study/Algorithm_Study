class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end()); // 2차원 벡터의 왼쪽원소를 기준으로 정렬
        
        vector<vector<int>> vv;
        vector<int> v;
        vv.push_back(intervals[0]);
        
        for(int i=1; i<intervals.size(); i++){
            if(vv.back()[1] < intervals[i][0]){ // 겹치는 것이 없는 경우
                vv.push_back(intervals[i]);
            }
            else{ // 겹치는 경우
                v.push_back(vv.back()[0]);
                v.push_back(max(intervals[i][1], vv.back()[1]));
                
                vv.pop_back();
                vv.push_back(v);
                
                v.clear();
            }
        }
        return vv;
    }
};