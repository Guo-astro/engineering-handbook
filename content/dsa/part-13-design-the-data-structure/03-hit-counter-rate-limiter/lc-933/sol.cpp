// LC 933. Number of Recent Calls
#include <deque>

class RecentCounter {
public:
    int ping(int t) {
        q.push_back(t);
        // Strict `<`: q.front == t - 3000 is INSIDE the window.
        while (!q.empty() && q.front() < t - 3000) {
            q.pop_front();
        }
        return static_cast<int>(q.size());
    }

private:
    std::deque<int> q;
};
