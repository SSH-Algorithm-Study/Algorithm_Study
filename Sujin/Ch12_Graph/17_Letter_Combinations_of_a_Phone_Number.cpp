#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> res; // 결과값을 담을 string 벡터
    string s; // 결과값의 원소를 담을 문자열 s
    vector<int> v;
    int size;
    
    vector<string> m = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    void DFS(int idx){
        if(idx==size){
            res.push_back(s);
        }
        else{
            for(int i=0; i<m[v[idx]].size(); i++){
                s.push_back(m[v[idx]][i]);
                cout<<s<<endl;
                DFS(idx+1);
                s.pop_back();
            }
        }
    }
    
    vector<string> letterCombinations(string digits) {
        size = digits.size();
        if(size==0) return res; // 예외처리
        
        for(int i=0; i<digits.size(); i++){
            int n = (int)(digits[i]-'0');
            v.push_back(n);
        }
        
        DFS(0);
        
        return res;
    }
};