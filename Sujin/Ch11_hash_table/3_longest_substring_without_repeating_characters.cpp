#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        int start = 1, res = 0; // 인덱스는 1부터 시작 -> 따라서 start = 1 (시작 부분의 원소를 가리킴)
        
        for(int i=0; i<s.size(); i++){
            if(map[s[i]]!=0 && start<=map[s[i]]){
                start = map[s[i]] + 1; // 중복된 원소의 다음 원소를 가리키기 (문자열의 첫 시작부분)
            }
            map[s[i]]=i+1;
            res = max(res, (i+1)-start+1); // 문자 개수: (i+1)-start+1 개
        }
        return res;
    }
};