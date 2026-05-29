// LC 17. Letter Combinations of a Phone Number
package main

var keypad = map[byte]string{
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
}

func letterCombinations(digits string) []string {
	result := []string{}
	if len(digits) == 0 {
		return result
	}
	path := make([]byte, 0, len(digits))

	var backtrack func(i int)
	backtrack = func(i int) {
		if i == len(digits) {
			// Snapshot: string(path) copies the bytes, so later mutations
			// to path do not corrupt the stored result. This is the Go
			// counterpart to []int slice-aliasing: byte slices alias too.
			result = append(result, string(path))
			return
		}
		for k := 0; k < len(keypad[digits[i]]); k++ {
			path = append(path, keypad[digits[i]][k]) // 1. CHOOSE
			backtrack(i + 1)                          // 2. EXPLORE
			path = path[:len(path)-1]                 // 3. UNCHOOSE
		}
	}
	backtrack(0)
	return result
}
