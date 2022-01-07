class Solution {
public:
    struct compare{
        bool operator()(int a, int b){
            string s1 = to_string(a); string s2 = to_string(b);
            return s1+s2 < s2+s1;
        }
    };
    
    string largestNumber(vector<int>& nums) {
        
        priority_queue<int, vector<int>, compare> pq;
        
        for(int i=0; i<nums.size(); i++){
            pq.push(nums[i]);
        }
        
        string s;
        
        while(!pq.empty()){
            s += to_string(pq.top());
            pq.pop();
        }
        
        if(s[0]=='0') return "0";
        else return s;
    }
};