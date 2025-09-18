interface Item {
    name: string;
    rating: number;
}

class MyHeap {
    _heep: Item[];
    size: number;
    indexes: { [key in string]: number };

    constructor(length: number) {
        this._heep = new Array(length);
        this.size = 0;
        this.indexes = {};
    }

    compare(a: Item, b: Item) { // O(1)
        if (a.rating === b.rating) {
            return a.name > b.name ? false : true;
        }
        return a.rating > b.rating
    }

    siffup(i: number) { // O(log n)
        while (i > 0) {
            const parentIndex = Math.floor((i - 1) / 2);
            if (this.compare(this._heep[i], this._heep[parentIndex])) {
                // swap
                const tmp = this._heep[i];
                this._heep[i] = this._heep[parentIndex];
                this._heep[parentIndex] = tmp;
                //update indexes
                this.indexes[this._heep[i].name] = i;
                this.indexes[this._heep[parentIndex].name] = parentIndex;
                i = parentIndex;
            } else {
                return;
            }
        }
    }

    siffdown(i: number) { // O(log n)
        const n = this.size;
        while (2 * i + 1 < n) {
            let swapI = 2 * i + 1;
            if (2 * i + 2 < n && this.compare(this._heep[2 * i + 2], this._heep[swapI])) {
                swapI = 2 * i + 2;
            }
            if (this.compare(this._heep[swapI], this._heep[i])) {
                // swap
                const tmp = this._heep[i];
                this._heep[i] = this._heep[swapI];
                this._heep[swapI] = tmp;
                // update indexes
                this.indexes[this._heep[i].name] = i;
                this.indexes[this._heep[swapI].name] = swapI;
                i = swapI;
            } else {
                return;
            }
        }
    }

    insert(item: Item) { // O(log n)
        this._heep[this.size] = item;
        this.indexes[item.name] = this.size;
        this.siffup(this.size);
        this.size++;
    }

    peak(): Item { // O(1)
        return this._heep[0];
    }

    update(name: string, rating: number) { // O(1)
        const i = this.indexes[name];
        this._heep[i].rating = rating;
        this.siffup(i);
        this.siffdown(i)
    }
}

class FoodRatings {
    // foodToCuisine: Map<string, string>
    // foodToRating: Map<string, number>
    // cuisineFoods: Map<string, Set<string>>
    heeps: { [key: string]: MyHeap } = {}
    foods: { [key: string]: string } = {}

    constructor(foods: string[], cuisines: string[], ratings: number[]) {
        // this.foodToCuisine = new Map()
        // this.foodToRating = new Map()
        // this.cuisineFoods = new Map()

        // for (let i = 0; i < foods.length; i++) {
        //     this.foodToCuisine.set(foods[i], cuisines[i])
        //     this.foodToRating.set(foods[i], ratings[i])
        // }

        // for (let i = 0; i < foods.length; i++) {
        //     let cuisine = cuisines[i]
        //     if (!this.cuisineFoods.has(cuisine)) {
        //         this.cuisineFoods.set(cuisine, new Set())
        //     }
        //     this.cuisineFoods.get(cuisine)!.add(foods[i])
        // }

        for (let i = 0; i < foods.length; ++i) {
            if (!(cuisines[i] in this.heeps)) {
                this.heeps[cuisines[i]] = new MyHeap(foods.length);
            }
            this.heeps[cuisines[i]].insert({ name: foods[i], rating: ratings[i] });
            this.foods[foods[i]] = cuisines[i];
        }
    }

    changeRating(food: string, newRating: number): void {
        // this.ratings[this.foods.indexOf(food)] = newRating

        // let cuisine = this.foodToCuisine.get(food)!
        // this.cuisineFoods.get(cuisine)!.delete(food)
        // this.foodToRating.set(food, newRating)
        // this.cuisineFoods.get(cuisine)!.add(food)

        const cuisine = this.foods[food];
        this.heeps[cuisine].update(food, newRating)
    }

    highestRated(cuisine: string): string {
        // let highRating = 0
        // let index = 0

        // for (let i = 0; i < this.cuisines.length; i++) {
        //     if (this.cuisines[i] === cuisine) {
        //         if (this.ratings[i] > highRating) {
        //             highRating = this.ratings[i]
        //             index = i
        //         } else if (this.ratings[i] === highRating && this.foods[index] > this.foods[i]) {
        //             index = i
        //         }
        //     }
        // }

        // return this.foods[index]


        // let foods = Array.from(this.cuisineFoods.get(cuisine)!)
        // foods.sort((a, b) => {
        //     let r1 = this.foodToRating.get(a)!
        //     let r2 = this.foodToRating.get(b)!
        //     if (r1 !== r2) return r2 - r1
        //     return a.localeCompare(b)
        // });
        // return foods[0]

        return this.heeps[cuisine].peak().name;
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */