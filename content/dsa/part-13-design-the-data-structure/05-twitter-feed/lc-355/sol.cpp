// LC 355. Design Twitter
// In-memory class with four operations. getNewsFeed runs a bounded
// k-way merge through a max-heap keyed on a monotonic timestamp.
// std::priority_queue is the rare structural win in C++: max-heap is
// the default, and tuples compare lexicographically, so the leading
// ts field drives the order without a custom comparator.
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <utility>
#include <tuple>

class Twitter {
public:
    Twitter() = default;

    void postTweet(int userId, int tweetId) {
        ++ts;
        tweets[userId].emplace_back(ts, tweetId);
    }

    std::vector<int> getNewsFeed(int userId) {
        std::unordered_set<int> authors = following[userId];
        authors.insert(userId);

        std::priority_queue<std::tuple<int, int, int, int>> heap;
        for (int a : authors) {
            auto it = tweets.find(a);
            if (it == tweets.end() || it->second.empty()) continue;
            int idx = static_cast<int>(it->second.size()) - 1;
            const auto& [t, tid] = it->second[idx];
            heap.emplace(t, tid, a, idx);
        }

        std::vector<int> feed;
        feed.reserve(FEED_CAP);
        while (!heap.empty() && static_cast<int>(feed.size()) < FEED_CAP) {
            auto [t, tid, a, idx] = heap.top();
            heap.pop();
            feed.push_back(tid);
            if (idx > 0) {
                int next = idx - 1;
                const auto& [pt, ptid] = tweets[a][next];
                heap.emplace(pt, ptid, a, next);
            }
        }
        return feed;
    }

    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        following[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        auto it = following.find(followerId);
        if (it != following.end()) it->second.erase(followeeId);
    }

private:
    static constexpr int FEED_CAP = 10;
    std::unordered_map<int, std::vector<std::pair<int, int>>> tweets;
    std::unordered_map<int, std::unordered_set<int>> following;
    int ts = 0;
};
