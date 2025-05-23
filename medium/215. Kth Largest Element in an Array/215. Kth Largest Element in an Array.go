package main

import (
	"container/heap"
)

type MinHeap []int

func (h MinHeap) Len() int { return len(h) }

func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }

func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() any {
	old := *h
	lastVal := old[len(old)-1]
	*h = old[:len(old)-1]
	return lastVal
}

func (h MinHeap) AsSlice() []int {
	return []int(h)
}

func findKthLargest(nums []int, k int) int {
	if len(nums) == 0 || k <= 0 || k > len(nums) {
		return -1
	}

	h := &MinHeap{}
	for _, num := range nums {
		if h.Len() < k {
			heap.Push(h, num)
		} else if num > (*h)[0] {
			heap.Pop(h)
			heap.Push(h, num)
		}
	}

	return (*h)[0]
}
