package main

import (
	"fmt"
	"slices"
	"sort"
)

func findArr(arr []int, k int) (result []int) {

	heap := make([]int, k)
	fmt.Printf("heap: %v\n", heap)

	for i := 0; i < k; i++ {
		heap = append(heap, 0)
	}
	count := map[int]int{}

	for _, v := range arr {
		count[v]++
	}

	for i, v := range count {
		if v > heap[0] {
			heap[0] = i
			sort.Slice(heap, func(i, j int) bool {
				return count[heap[i]] < count[heap[j]]
			})
			slices.Sort(heap)
		}
	}

	return heap
}

func main() {
	// k := 5
	// heap := make([]int, k)
	// fmt.Printf("heap: %v\n", heap[0])
	// return

}
