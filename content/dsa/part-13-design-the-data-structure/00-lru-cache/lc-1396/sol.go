// LC 1396. Design Underground System
// Two cooperating hash maps — the dual-structure design pattern
// stripped to its essence.
package main

type checkInRec struct {
	start string
	t     int
}

type avgRec struct {
	sum   int
	count int
}

type UndergroundSystem struct {
	checkIns  map[int]checkInRec
	checkOuts map[string]*avgRec
}

func ConstructorUndergroundSystem() UndergroundSystem {
	return UndergroundSystem{
		checkIns:  make(map[int]checkInRec),
		checkOuts: make(map[string]*avgRec),
	}
}

func (u *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	u.checkIns[id] = checkInRec{start: stationName, t: t}
}

func (u *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	in := u.checkIns[id]
	delete(u.checkIns, id)
	key := in.start + "->" + stationName
	rec, ok := u.checkOuts[key]
	if !ok {
		rec = &avgRec{}
		u.checkOuts[key] = rec
	}
	rec.sum += t - in.t
	rec.count++
}

func (u *UndergroundSystem) GetAverageTime(startStation, endStation string) float64 {
	rec := u.checkOuts[startStation+"->"+endStation]
	return float64(rec.sum) / float64(rec.count)
}
