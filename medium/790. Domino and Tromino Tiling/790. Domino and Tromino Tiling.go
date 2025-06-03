package main

const MOD = 1_000_000_007

func numTilings(n int) int {
	FF, F, T, B := 1, 1, 0, 0

	for i := 2; i <= n; i++ {
		FF, F, T, B = F, (F+FF+T+B)%MOD, (FF+B)%MOD, (FF+T)%MOD
	}

	return F
}
