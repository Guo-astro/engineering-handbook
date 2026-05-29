// LC 146. LRU Cache
#include <list>
#include <unordered_map>
#include <utility>

class LRUCache {
public:
    explicit LRUCache(int capacity) : capacity_(capacity) {}

    int get(int key) {
        auto it = map_.find(key);
        if (it == map_.end()) {
            return -1;
        }
        // splice moves the node to the front of order_ in O(1) without
        // invalidating the iterator stored in map_; this is why std::list
        // is the right C++ idiom.
        order_.splice(order_.begin(), order_, it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = map_.find(key);
        if (it != map_.end()) {
            it->second->second = value;
            order_.splice(order_.begin(), order_, it->second);
            return;
        }
        if (static_cast<int>(map_.size()) == capacity_) {
            map_.erase(order_.back().first);
            order_.pop_back();
        }
        order_.emplace_front(key, value);
        map_[key] = order_.begin();
    }

private:
    int capacity_;
    std::list<std::pair<int, int>> order_;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> map_;
};
