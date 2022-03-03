class Solution {
public:
    int sum=0;
    
    void sum_DFS(TreeNode* root){
        if(!root) return;
        
        if(root) sum += root->val;
        
        sum_DFS(root->left);
        sum_DFS(root->right);
    }
    
    void change_DFS(TreeNode* root){ // 전위순회로 트리 바꾸기
        if(!root) return;
        
        change_DFS(root->left);
        int tmp = root->val;
        root->val = sum;
        sum -= tmp;
        change_DFS(root->right);
        
    }
    
    TreeNode* bstToGst(TreeNode* root) {
        sum_DFS(root);
        change_DFS(root);
        return root;
    }
};