#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_map<char, int> map;
        
        for(int i=0; i<jewels.size(); i++){
            map[jewels[i]]=1;
        }
        
        int count = 0;
        for(int i=0; i<stones.size(); i++){
            if(map[stones[i]]==1) count++;
        }
        return count;
    }
};