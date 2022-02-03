class Solution {
public:
    static bool cmp(vector<int> a, vector<int> b){
        if(a[0]!=b[0]) return a[0]>b[0]; // 내림차순
        else // a[0]==b[0]
            return a[1]<b[1]; // 오름차순
    }
    
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), cmp);
        vector<vector<int>> res;
        
        res.push_back(people[0]);
        
        for(int i=1; i<people.size(); i++){
            if(res.back()[0]==people[i][0]) res.push_back(people[i]);
            else{
                res.insert(res.begin()+people[i][1], people[i]);
            }
        }
        
        
        return res;
    }
};
