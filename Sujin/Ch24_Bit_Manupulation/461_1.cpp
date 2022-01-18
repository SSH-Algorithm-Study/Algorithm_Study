class Solution {
public:
    int hammingDistance(int x, int y) {
        int res = x ^ y; // res의 비트에는 x y 에서 다른 경우만 1로 되어 있음
        
        int tmp=1, cnt=0;
        // res의 비트 중 1이 몇개 인지 계산하기
        for(int i=1; i<=32; i++){
            if(res & tmp) cnt++;
            if(i==32) break;
            tmp = tmp<<1; // tmp*=2; 와 동일
        }
        return cnt;
    }
};
