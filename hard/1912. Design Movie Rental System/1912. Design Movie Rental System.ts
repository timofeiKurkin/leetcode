class MovieRentingSystem {
    private price: Map<string, number>
    private movieShops: Map<number, [number, number][]>
    private rented: Set<string>

    constructor(n: number, entries: number[][]) {
        this.price = new Map()
        this.movieShops = new Map()
        this.rented = new Set()

        for (const [shop, movie, p] of entries) {
            const key = this.encode(shop, movie)
            this.price.set(key, p)

            const movieShop = this.movieShops.get(movie) || []
            if (!movieShop.length) this.movieShops.set(movie, movieShop)
            movieShop.push([p, shop])
        }

        for (const arr of this.movieShops.values()) {
            arr.sort((a, b) => (a[0] - b[0]) || (a[1] - b[1]))
        }
    }

    private encode(shop: number, movie: number): string {
        return `${shop}#${movie}`
    }

    search(movie: number): number[] {
        const res: number[] = []
        const arr = this.movieShops.get(movie) || []

        for (const [_, shop] of arr) {
            if (!this.rented.has(this.encode(shop, movie))) {
                res.push(shop)
                if (res.length === 5) break
            }
        }

        return res
    }

    rent(shop: number, movie: number): void {
        this.rented.add(this.encode(shop, movie))
    }

    drop(shop: number, movie: number): void {
        this.rented.delete(this.encode(shop, movie))
    }

    report(): number[][] {
        const temp: [number, number, number][] = []

        for (const key of this.rented) {
            const [shopStr, movieStr] = key.split('#');
            const shop = Number(shopStr);
            const movie = Number(movieStr);
            const p = this.price.get(key)!;

            temp.push([p, shop, movie]);
        }

        temp.sort((a, b) => (a[0] - b[0]) || (a[1] - b[1]) || (a[2] - b[2]));

        const res: number[][] = [];
        for (let i = 0; i < temp.length && i < 5; i++) {
            res.push([temp[i][1], temp[i][2]]);
        }
        return res;
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = new MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */