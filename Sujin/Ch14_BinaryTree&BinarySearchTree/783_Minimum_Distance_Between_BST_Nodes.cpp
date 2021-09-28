class Solution {
public:
    vector<int> v;
    
    void DFS(TreeNode* root){
        if(!root) return;
        if(root) v.push_back(root->val);
        
        DFS(root->left);
        DFS(root->right);
    }
    
    int minDiffInBST(TreeNode* root) {
        DFS(root);
        
        sort(v.begin(), v.end());
        vector<int>::iterator it;
        int gap = 100001;
        int tmp = v[0];
        
        for(it=v.begin(); it!=v.end()-1; it++){
            int tmp_gap = abs(*it-*(it+1));
            gap = min(gap, tmp_gap); // sliding window 이용
        }
        return gap;
    }
};