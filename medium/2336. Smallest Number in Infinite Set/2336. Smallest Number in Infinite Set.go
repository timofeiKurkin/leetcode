package main

import "container/heap"

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

type SmallestInfiniteSet struct {
	smallest int
	set      map[int]bool
	h        *MinHeap
}

func Constructor() SmallestInfiniteSet {
	h := &MinHeap{}
	heap.Init(h)
	return SmallestInfiniteSet{0, map[int]bool{}, h}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	if this.h.Len() > 0 {
		v := heap.Pop(this.h).(int)
		this.set[v] = false
		return v
	}

	this.smallest += 1
	return this.smallest
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if num <= this.smallest && !this.set[num] {
		this.set[num] = true
		heap.Push(this.h, num)
	}
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */
