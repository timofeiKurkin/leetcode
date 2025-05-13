package main

type RecentCounter struct {
	r []int
}

func Constructor() RecentCounter {
	return RecentCounter{}
}

func (this *RecentCounter) Ping(t int) int {
	this.r = append(this.r, t)
	for this.r[0] < t-3000 {
		this.r = this.r[1:]
	}
	return len(this.r)
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
