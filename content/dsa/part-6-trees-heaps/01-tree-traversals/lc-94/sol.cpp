// LC 94. Binary Tree Inorder Traversal
#include <algorithm>
#include <stack>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Recursive inorder — the canonical LC 94 entry point.
    std::vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> out;
        inorder(root, out);
        return out;
    }

    // Iterative inorder. Push left chain, pop, pivot right.
    std::vector<int> inorderIterative(TreeNode* root) {
        std::vector<int> out;
        std::stack<TreeNode*> st;
        TreeNode* cur = root;
        while (cur || !st.empty()) {
            while (cur) {
                st.push(cur);
                cur = cur->left;
            }
            cur = st.top(); st.pop();
            out.push_back(cur->val);
            cur = cur->right;                    // pivot to right subtree
        }
        return out;
    }

    // Iterative preorder. Push right BEFORE left so left pops next.
    std::vector<int> preorderIterative(TreeNode* root) {
        std::vector<int> out;
        if (!root) return out;
        std::stack<TreeNode*> st;
        st.push(root);
        while (!st.empty()) {
            auto* n = st.top(); st.pop();
            out.push_back(n->val);
            if (n->right) st.push(n->right);
            if (n->left)  st.push(n->left);
        }
        return out;
    }

    // Iterative postorder via the two-stack / reverse trick.
    std::vector<int> postorderIterative(TreeNode* root) {
        std::vector<int> out;
        if (!root) return out;
        std::stack<TreeNode*> st;
        st.push(root);
        while (!st.empty()) {
            auto* n = st.top(); st.pop();
            out.push_back(n->val);
            if (n->left)  st.push(n->left);
            if (n->right) st.push(n->right);
        }
        std::reverse(out.begin(), out.end());
        return out;
    }

private:
    void inorder(TreeNode* n, std::vector<int>& out) {
        if (!n) return;
        inorder(n->left, out);
        out.push_back(n->val);                   // visit
        inorder(n->right, out);
    }
};
