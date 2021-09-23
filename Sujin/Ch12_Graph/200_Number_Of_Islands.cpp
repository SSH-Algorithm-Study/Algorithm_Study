#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int ch[301][301]={0, };
    vector<vector<char>> v;
    int maxi, maxj;
    int res=0;
    
    void DFS(int i, int j){
            ch[i][j]=1;
            
            if(i+1<maxi && v[i+1][j]=='1' && ch[i+1][j]==0) DFS(i+1, j);
            if(j+1<maxj && v[i][j+1]=='1' && ch[i][j+1]==0) DFS(i, j+1);
            if(i-1>=0 && v[i-1][j]=='1' && ch[i-1][j]==0) DFS(i-1, j);
            if(j-1>=0 && v[i][j-1]=='1' && ch[i][j-1]==0) DFS(i, j-1);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        v.assign(grid.begin(), grid.end());
        maxi = grid.size();
        maxj = grid[0].size();
        for(int i=0; i<maxi; i++){
            for(int j=0; j<maxj; j++){
                if(v[i][j]=='1' && ch[i][j]==0){
                    res++;
                    DFS(i, j);
                }
            }
        }
        return res;
    }
    
};