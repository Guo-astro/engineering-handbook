// LC 1396. Design Underground System
// Two cooperating hash maps — the dual-structure design pattern
// stripped to its essence. checkIns: id -> (start, t). checkOuts:
// "start->end" -> {sum, count}.
import java.util.HashMap;
import java.util.Map;

class UndergroundSystem {
    private static final class Trip {
        final String start;
        final int t;
        Trip(String start, int t) { this.start = start; this.t = t; }
    }

    private static final class Avg {
        long sum = 0;
        int count = 0;
    }

    private final Map<Integer, Trip> checkIns = new HashMap<>();
    private final Map<String, Avg> checkOuts = new HashMap<>();

    public void checkIn(int id, String stationName, int t) {
        checkIns.put(id, new Trip(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        Trip in = checkIns.remove(id);
        String key = in.start + "->" + stationName;
        Avg avg = checkOuts.computeIfAbsent(key, k -> new Avg());
        avg.sum += (t - in.t);
        avg.count += 1;
    }

    public double getAverageTime(String startStation, String endStation) {
        Avg avg = checkOuts.get(startStation + "->" + endStation);
        return (double) avg.sum / avg.count;
    }
}
