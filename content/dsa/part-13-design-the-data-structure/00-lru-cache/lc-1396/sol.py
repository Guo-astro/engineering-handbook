# LC 1396. Design Underground System
# Two cooperating hash maps — the same skeleton as LRU's index_+order_,
# stripped to its essence. checkIns is keyed by passenger id (lookup
# the open trip); checkOuts is keyed by (start, end) station pair
# (aggregate completed trips for an average).
from collections import defaultdict


class UndergroundSystem:
    def __init__(self) -> None:
        # passenger id -> (start_station, t)
        self.check_ins: dict[int, tuple[str, int]] = {}
        # (start, end) -> (sum_of_durations, num_trips)
        self.check_outs: dict[tuple[str, str], tuple[int, int]] = defaultdict(
            lambda: (0, 0)
        )

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t0 = self.check_ins.pop(id)
        total, n = self.check_outs[(start, stationName)]
        self.check_outs[(start, stationName)] = (total + (t - t0), n + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, n = self.check_outs[(startStation, endStation)]
        return total / n
