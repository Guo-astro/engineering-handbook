package main

func countFreqs(s string) map[byte]int {
	freq := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		freq[s[i]]++ // map zero value for int is 0
	}
	return freq
}
