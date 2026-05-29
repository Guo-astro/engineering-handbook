// LC 1396. Design Underground System
// Two cooperating hash maps — the dual-structure design pattern
// stripped to its essence.
#include <string>
#include <unordered_map>
#include <utility>

class UndergroundSystem {
public:
    void checkIn(int id, std::string stationName, int t) {
        checkIns_[id] = {std::move(stationName), t};
    }

    void checkOut(int id, std::string stationName, int t) {
        auto it = checkIns_.find(id);
        const auto& [start, t0] = it->second;
        auto& slot = checkOuts_[start + "->" + stationName];
        slot.first += (t - t0);
        slot.second += 1;
        checkIns_.erase(it);
    }

    double getAverageTime(std::string startStation, std::string endStation) {
        const auto& slot = checkOuts_[startStation + "->" + endStation];
        return static_cast<double>(slot.first) / slot.second;
    }

private:
    std::unordered_map<int, std::pair<std::string, int>> checkIns_;
    std::unordered_map<std::string, std::pair<long long, int>> checkOuts_;
};
