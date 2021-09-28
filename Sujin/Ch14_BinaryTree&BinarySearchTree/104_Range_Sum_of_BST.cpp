class Solution {
public:
    int sum=0;
    int l, h;
    
    void DFS(TreeNode* root){
        if(!root) return;
        
        if((root->val >= l) && (root->val <= h)){
            sum += root->val;
        }
        DFS(root->left);
        DFS(root->right);
    }
    
    int rangeSumBST(TreeNode* root, int low, int high) {
        l = low;
        h = high;
        
        DFS(root);
        return sum;
    }
};