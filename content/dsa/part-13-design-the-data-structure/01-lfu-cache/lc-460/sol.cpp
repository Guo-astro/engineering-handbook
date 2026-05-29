// LC 460. LFU Cache
#include <list>
#include <tuple>
#include <unordered_map>

class LFUCache {
public:
    LFUCache(int capacity) : cap_(capacity), size_(0), minFreq_(0) {}

    int get(int key) {
        auto it = keyMap_.find(key);
        if (it == keyMap_.end()) return -1;
        int val  = std::get<0>(it->second);
        int freq = std::get<1>(it->second);
        auto listIt = std::get<2>(it->second);
        freqMap_[freq].erase(listIt);
        if (freqMap_[freq].empty()) {
            freqMap_.erase(freq);
            if (minFreq_ == freq) minFreq_++;
        }
        auto& nextList = freqMap_[freq + 1];
        nextList.push_back(key);
        keyMap_[key] = std::make_tuple(val, freq + 1, std::prev(nextList.end()));
        return val;
    }

    void put(int key, int value) {
        if (cap_ <= 0) return;
        auto it = keyMap_.find(key);
        if (it != keyMap_.end()) {
            std::get<0>(it->second) = value;
            get(key);
            return;
        }
        if (size_ == cap_) {
            int evictKey = freqMap_[minFreq_].front();
            freqMap_[minFreq_].pop_front();
            if (freqMap_[minFreq_].empty()) freqMap_.erase(minFreq_);
            keyMap_.erase(evictKey);
            size_--;
        }
        auto& bucket = freqMap_[1];
        bucket.push_back(key);
        keyMap_[key] = std::make_tuple(value, 1, std::prev(bucket.end()));
        minFreq_ = 1;
        size_++;
    }

private:
    int cap_, size_, minFreq_;
    std::unordered_map<int, std::tuple<int, int, std::list<int>::iterator>> keyMap_;
    std::unordered_map<int, std::list<int>> freqMap_;
};
