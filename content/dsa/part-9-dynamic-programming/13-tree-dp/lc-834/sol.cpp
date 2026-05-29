// LC 834. Sum of Distances in Tree
// implements the re-rooting technique
//  (pattern extension).
#include <vector>

class Solution {
public:
    std::vector<int> sumOfDistancesInTree(int n, std::vector<std::vector<int>>& edges) {
        if (n == 1) return std::vector<int>{0};
        adj_.assign(n, {});
        for (const auto& e : edges) {
            adj_[e[0]].push_back(e[1]);
            adj_[e[1]].push_back(e[0]);
        }
        count_.assign(n, 1);
        answer_.assign(n, 0);
        n_ = n;
        // Pass 1: post-order — fill count[] and answer[0].
        post(0, -1);
        // Pass 2: pre-order — re-root from u to each child v in O(1).
        pre(0, -1);
        return answer_;
    }

private:
    std::vector<std::vector<int>> adj_;
    std::vector<int> count_;
    std::vector<int> answer_;
    int n_;

    void post(int u, int parent) {
        for (int v : adj_[u]) {
            if (v == parent) continue;
            post(v, u);
            count_[u]  += count_[v];
            answer_[u] += answer_[v] + count_[v];
        }
    }

    void pre(int u, int parent) {
        for (int v : adj_[u]) {
            if (v == parent) continue;
            // Re-root: count[v] nodes get 1 closer, (n - count[v]) get 1 farther.
            answer_[v] = answer_[u] - count_[v] + (n_ - count_[v]);
            pre(v, u);
        }
    }
};
