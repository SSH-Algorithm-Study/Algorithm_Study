#include <iostream>
#include <vector>
#include <algorithm>
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
    int longestUnivaluePath(TreeNode* root){
        DFS(root, -1001);
        return res;
    }

    int DFS(TreeNode*root, int parentNum){
        if(root==NULL) return 0;

        int l = DFS(root->left, root->val);
        int r = DFS(root->right, root->val);

        //최댓값 갱신 : root를 루트노드로 했을 때 나올 수 있는 최댓값
        res = max(res, l+r);

        // DFS가 반환해야 하는 값

        if(root->val == parentNum) return max(l, r)+1;
        return 0;
    }
};