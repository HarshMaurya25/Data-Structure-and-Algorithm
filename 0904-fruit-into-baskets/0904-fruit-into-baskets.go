func totalFruit(fruits []int) int {
	count := make(map[int]int)
	left := 0
	ans := 0

	for right, fruit := range fruits {
		count[fruit]++

		for len(count) > 2 {
			count[fruits[left]]--

			if count[fruits[left]] == 0 {
				delete(count, fruits[left])
			}

			left++
		}

		ans = max(ans, right-left+1)
	}

	return ans
}
