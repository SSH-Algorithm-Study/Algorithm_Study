/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    queue<string> q;
    string s;
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        
        if (root == NULL) return "null";
        string tmp;
        tmp += to_string(root -> val);
        string serial_left = serialize(root -> left);
        string serial_right = serialize(root -> right);
        return tmp + " " + serial_left + " " + serial_right;
    }
    
    TreeNode* d_helper(queue<string> &q){
        if(q.empty()) return NULL;
        
        string s = q.front();
        q.pop();
        if(s=="null") return NULL;
        
        int val = stoi(s);
        TreeNode* node = new TreeNode(val);
        node->left = d_helper(q);
        node->right = d_helper(q);
        
        return node;
    }

    TreeNode* deserialize(string data) {
        cout<<data<<endl;
        queue<string> q;
        string tmp;
        
        for(int i=0; i<data.size(); i++){
            if(data[i]!=' ') tmp.push_back(data[i]);
            else{ // 공백일때
                q.push(tmp);
                tmp.clear();
            }
        }
        
        return d_helper(q);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));