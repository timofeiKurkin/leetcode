package main

import (
	"sort"
)

func suggestedProducts(products []string, searchWord string) [][]string {
	res := [][]string{}
	sort.Strings(products)
	prev := products

	for i := 0; i < len(searchWord); i++ {
		temp := []string{}
		for _, product := range prev {
			if len(products) > i && product[i] == searchWord[i] {
				temp = append(temp, product)
			}
		}

		prev = temp
		if len(temp) <= 3 {
			res = append(res, temp)
		} else {
			res = append(res, temp[:3])
		}
	}

	return res
}
