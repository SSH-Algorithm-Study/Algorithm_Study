class Solution {
public:
    struct cmp{
        bool operator() (pair<int, int>&a, pair<int, int>&b){
            if(a.second==b.second){
                return a.first < b.first;
            }
            else{
                return a.second < b.second;
            }
        }
    };
    
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res; // 결과벡터
        priority_queue<pair<int, int>, vector<pair<int, int> >, cmp> pq; // <idx, nums[idx]> 저장
        int i;
        
        // 첫 번째 순회만 예외처리
        for(i=0; i<k; i++) pq.push({i, nums[i]});
        res.push_back(pq.top().second);
        
        // 두 번째 이후부터
        for(; i<nums.size(); i++){
            pq.push({i, nums[i]});
            while(pq.top().first <= i-k){
                pq.pop();
            }
            res.push_back(pq.top().second);
        }
        return res;
    }
};
