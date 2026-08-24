package main

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}

	m := make(map[byte]int)
	maxLen := 0
	j := 0

	for i := 0; i < len(s); i++ {
		char := s[i]

		lastSeenIndex, exists := m[char]
		if exists && lastSeenIndex >= j {
			j = lastSeenIndex + 1
		}

		m[char] = i

		currentWindowSize := i - j + 1
		if currentWindowSize > maxLen {
			maxLen = currentWindowSize
		}
	}

	return maxLen
}
