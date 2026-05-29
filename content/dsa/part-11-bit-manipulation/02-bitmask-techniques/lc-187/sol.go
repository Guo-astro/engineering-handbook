// LC 187. Repeated DNA Sequences
package main

func findRepeatedDnaSequences(s string) []string {
	if len(s) < 10 {
		return []string{}
	}
	var code [26]int
	code['A'-'A'] = 0
	code['C'-'A'] = 1
	code['G'-'A'] = 2
	code['T'-'A'] = 3
	mask := 0
	const MASK20 = (1 << 20) - 1
	seen := make(map[int]int)
	answer := []string{}
	for i := 0; i < len(s); i++ {
		mask = ((mask << 2) | code[s[i]-'A']) & MASK20
		if i >= 9 {
			seen[mask]++
			if seen[mask] == 2 {
				answer = append(answer, s[i-9:i+1])
			}
		}
	}
	return answer
}
