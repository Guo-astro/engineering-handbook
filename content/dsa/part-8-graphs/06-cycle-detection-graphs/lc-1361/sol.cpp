// LC 1361. Validate Binary Tree Nodes
#include <vector>
#include <queue>

class Solution {
public:
    bool validateBinaryTreeNodes(int n, std::vector<int>& leftChild, std::vector<int>& rightChild) {
        std::vector<int> inDegree(n, 0);
        for (int c : leftChild) if (c != -1) inDegree[c]++;
        for (int c : rightChild) if (c != -1) inDegree[c]++;

        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (inDegree[i] == 0) {
                if (root != -1) return false;
                root = i;
            } else if (inDegree[i] > 1) {
                return false;
            }
        }
        if (root == -1) return false;

        std::vector<char> seen(n, 0);
        seen[root] = 1;
        int visitedCount = 1;
        std::queue<int> q;
        q.push(root);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            int kids[2] = { leftChild[u], rightChild[u] };
            for (int v : kids) {
                if (v == -1) continue;
                if (seen[v]) return false;          // cycle witness
                seen[v] = 1;
                visitedCount++;
                q.push(v);
            }
        }
        return visitedCount == n;
    }
};
