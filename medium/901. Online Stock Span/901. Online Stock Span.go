package main

type StockSpanner struct {
	stack [][]int
}

func Constructor() StockSpanner {
	return StockSpanner{stack: [][]int{}}
}

func (this *StockSpanner) Next(price int) int {
	if len(this.stack) == 0 || this.stack[len(this.stack)-1][1] > price {
		this.stack = append(this.stack, []int{1, price})
		return 1
	} else {
		span := 0

		for len(this.stack) > 0 && this.stack[len(this.stack)-1][1] <= price {
			prevPrice := this.stack[len(this.stack)-1]
			this.stack = this.stack[:len(this.stack)-1]
			span += prevPrice[0]
		}

		this.stack = append(this.stack, []int{span + 1, price})

		return span + 1
	}
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
