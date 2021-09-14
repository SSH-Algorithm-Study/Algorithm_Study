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
    void DFS(TreeNode* root){
        if(root==NULL) return;

        DFS(root->left);
        DFS(root->right);

        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;
    }

    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL) return NULL; // 예외처리

        TreeNode* res = root;
        DFS(root);
        return res;
    }
};