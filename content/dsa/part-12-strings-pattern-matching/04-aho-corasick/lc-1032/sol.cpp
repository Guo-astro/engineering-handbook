// LC 1032. Stream of Characters

#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

class StreamChecker {
    std::vector<std::unordered_map<char, int>> children;
    std::vector<int> fail;
    std::vector<bool> hasOutput;
    int node = 0;  // current automaton state

public:
    StreamChecker(std::vector<std::string>& words) {
        children.emplace_back();
        fail.push_back(0);
        hasOutput.push_back(false);

        // 1) Build the trie.
        for (const std::string& pat : words) {
            int cur = 0;
            for (char ch : pat) {
                auto it = children[cur].find(ch);
                int nxt;
                if (it == children[cur].end()) {
                    nxt = (int)children.size();
                    children.emplace_back();
                    fail.push_back(0);
                    hasOutput.push_back(false);
                    children[cur][ch] = nxt;
                } else {
                    nxt = it->second;
                }
                cur = nxt;
            }
            hasOutput[cur] = true;
        }

        // 2) Build failure links via BFS.
        std::queue<int> q;
        for (auto& [ch, child] : children[0]) {
            fail[child] = 0;
            q.push(child);
        }
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto& [ch, v] : children[u]) {
                q.push(v);
                int f = fail[u];
                while (f != 0 && children[f].find(ch) == children[f].end()) {
                    f = fail[f];
                }
                int fv = 0;
                auto it = children[f].find(ch);
                if (it != children[f].end()) fv = it->second;
                if (fv == v) fv = 0;
                fail[v] = fv;
                // Output inheritance.
                if (hasOutput[fail[v]]) hasOutput[v] = true;
            }
        }
    }

    bool query(char letter) {
        while (node != 0 && children[node].find(letter) == children[node].end()) {
            node = fail[node];
        }
        auto it = children[node].find(letter);
        node = (it == children[node].end()) ? 0 : it->second;
        return hasOutput[node];
    }
};
