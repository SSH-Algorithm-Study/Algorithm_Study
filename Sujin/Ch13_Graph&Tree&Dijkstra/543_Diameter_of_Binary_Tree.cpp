#include <iostream>
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
    int ans = 0; // answer

    int DFS(TreeNode* node){
        if(node==NULL) return 0;

        int left = DFS(node->left);
        int right = DFS(node->right);

        ans = max(ans, left+right); // 최댓값 갱신
        return max(left, right)+1; // DFS내에서 반환해야하는 값
    }

    int diameterOfBinaryTree(TreeNode* root){
        if(root==NULL) return 0; // root==[]인 경우의 예외처리

        DFS(root);
        return ans;
    }
};