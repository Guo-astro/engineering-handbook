// LC 621. Task Scheduler
#include <vector>
#include <queue>
#include <deque>
#include <utility>

class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
        if (n == 0) return static_cast<int>(tasks.size());
        int counts[26] = {0};
        for (char t : tasks) counts[t - 'A']++;
        // std::priority_queue<int> is a max-heap by default; the rare
        // structural win where C++ is the shorter language.
        std::priority_queue<int> heap;
        for (int c : counts) if (c > 0) heap.push(c);
        std::deque<std::pair<int, int>> cooldown;  // (remaining, ready_time)
        int time = 0;
        while (!heap.empty() || !cooldown.empty()) {
            ++time;
            if (!heap.empty()) {
                int remaining = heap.top() - 1;
                heap.pop();
                if (remaining > 0) {
                    cooldown.emplace_back(remaining, time + n);
                }
            }
            if (!cooldown.empty() && cooldown.front().second == time) {
                heap.push(cooldown.front().first);
                cooldown.pop_front();
            }
        }
        return time;
    }
};
