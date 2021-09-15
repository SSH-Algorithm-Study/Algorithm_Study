#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int res = 0;
    void DFS(TreeNode* n, int sum){
        if(sum > res) res = sum; // res에 sum의 최댓값을 계속 갱신하기
        
        if(n->left!=NULL) DFS(n->left, sum+1);
        if(n->right!=NULL) DFS(n->right, sum+1);
    }
    
    int maxDepth(TreeNode* root) {
        if(root==NULL) return 0; // 예외처리
        
        DFS(root, 1);
        return res;
    }
};