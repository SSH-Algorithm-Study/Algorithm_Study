class Solution {
public:
    int hammingDistance(int x, int y) {
        bitset<32> bit1(x);
        bitset<32> bit2(y);
        int res=0;
        
        for(int i=0; i<32; i++){
            if(bit1[i]!=bit2[i]) res++;
        }
        return res;
    }
};
