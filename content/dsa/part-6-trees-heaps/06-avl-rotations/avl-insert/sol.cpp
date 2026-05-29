// LC: none — chapter mechanic (AVL insert with rebalance)
#include <algorithm>
#include <cstdlib>

struct Node {
    int key;
    Node* left;
    Node* right;
    int height;
    explicit Node(int k) : key(k), left(nullptr), right(nullptr), height(1) {}
};

inline int avlHeight(const Node* n) { return n ? n->height : 0; }

inline int balanceFactor(const Node* n) {
    return avlHeight(n->left) - avlHeight(n->right);
}

inline void updateHeight(Node* n) {
    n->height = 1 + std::max(avlHeight(n->left), avlHeight(n->right));
}

inline Node* rotateRight(Node* y) {                 // fixes LL
    Node* x = y->left;
    Node* t2 = x->right;
    x->right = y;
    y->left = t2;
    updateHeight(y);
    updateHeight(x);
    return x;
}

inline Node* rotateLeft(Node* x) {                  // fixes RR
    Node* y = x->right;
    Node* t2 = y->left;
    y->left = x;
    x->right = t2;
    updateHeight(x);
    updateHeight(y);
    return y;
}

inline Node* insert(Node* root, int key) {
    if (root == nullptr) return new Node(key);
    if (key < root->key)      root->left  = insert(root->left,  key);
    else if (key > root->key) root->right = insert(root->right, key);
    else return root;

    updateHeight(root);
    int bf = balanceFactor(root);

    if (bf >  1 && root->left  && key < root->left->key)         // LL
        return rotateRight(root);
    if (bf < -1 && root->right && key > root->right->key)        // RR
        return rotateLeft(root);
    if (bf >  1 && root->left  && key > root->left->key) {       // LR
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }
    if (bf < -1 && root->right && key < root->right->key) {      // RL
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }
    return root;
}
