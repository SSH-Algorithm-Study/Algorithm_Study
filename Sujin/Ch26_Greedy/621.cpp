class Solution {
public:
    struct cmp{
        bool operator() (pair<char, int> &x, pair<char, int> &y){
            return x.second < y.second;
        }
    };
    
    int leastInterval(vector<char>& tasks, int n) {
        map<char, int> m;
        for(int i=0; i<tasks.size(); i++) m[tasks[i]]++;
        
        priority_queue<pair<char, int>, vector<pair<char, int>>, cmp> pq, tmp;
        for(auto item: m) pq.push(item);
        
        int res=0;
        while(!pq.empty()){
            int i;
            for(i=0; i<=n && !pq.empty(); i++){
                if(pq.top().second > 1){
                    tmp.push({pq.top().first, pq.top().second-1}); // 재활용 할 것만 tmp에 넣기
                }
                res++;
                pq.pop();
            }
            if(i!=n+1 && (pq.empty() && !tmp.empty())) res+=((n+1)-i);
            while(!tmp.empty()){
                pq.push(tmp.top());
                tmp.pop();
            }
        } // 전체 while문 끝
        
        
        return res;
    }
};
