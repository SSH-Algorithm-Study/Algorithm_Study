class Solution {
public:
    int getSum(int a, int b) {
        int res=1;
        int arr[32]={0, };
        int carry=0;
        
        for(int i=0; i<32; i++){
            // 0 0
            if(!(a&res) && !(b&res)){
                arr[i]=carry;
                carry=0;
            }
            // 1 1
            else if((a&res)!=0 && (b&res)!=0){
                if(carry) arr[i]=1;
                else arr[i]=0;
                
                carry=1; // 캐리 발생
            }
            // 0 1 또는 1 0
            else{
                if(carry){
                    arr[i]=0;
                    carry=1;
                }
                else{
                    arr[i]=1;
                    carry=0;
                }
            }
            if(i==31) break;
            res = res << 1;
        } // for문 끝
        
        
        res=1;
        int sum=0;
        for(int i=0; i<32; i++){
            sum = sum | res*arr[i];
            if(i==31) break;
            res = res << 1; // res*=2; 와 동일
        }
        
        return sum;
    }
};
