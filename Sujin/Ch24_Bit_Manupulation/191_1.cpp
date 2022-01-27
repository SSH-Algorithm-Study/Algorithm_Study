class Solution {
public:
    int hammingWeight(uint32_t n) {
        int b=1, cnt=0; // cnt는 1의 개수
        for(int i=0; i<32; i++){
            if(n & b) cnt++;
            if(i==31) break;
            b = b<<1;
        }
        return cnt;
    }
};
