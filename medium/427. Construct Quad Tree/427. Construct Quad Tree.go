/**
 * Definition for a QuadTree node.
 */
package main

import "fmt"

type Node struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *Node
	TopRight    *Node
	BottomLeft  *Node
	BottomRight *Node
}

func quad_tree(grid [][]int, x1, x2, y1, y2 int) *Node {
	if x1 == x2 && y1 == y2 {
		return &Node{Val: grid[y1][x1] == 1, IsLeaf: true}
	}

	xMiddle := (x1 + x2) / 2
	yMiddle := (y1 + y2) / 2

	topLeft := quad_tree(grid, x1, xMiddle, y1, yMiddle)
	topRight := quad_tree(grid, xMiddle+1, x2, y1, yMiddle)
	bottomLeft := quad_tree(grid, x1, xMiddle, yMiddle+1, y2)
	bottomRight := quad_tree(grid, xMiddle+1, x2, yMiddle+1, y2)

	if topLeft.IsLeaf && topRight.IsLeaf && bottomLeft.IsLeaf && bottomRight.IsLeaf {
		if topLeft.Val == topRight.Val && topRight.Val == bottomLeft.Val && bottomLeft.Val == bottomRight.Val {
			return &Node{Val: topLeft.Val, IsLeaf: true}
		}
	}

	return &Node{Val: true, IsLeaf: false, TopLeft: topLeft, TopRight: topRight, BottomLeft: bottomLeft, BottomRight: bottomRight}
}

func construct(grid [][]int) *Node {
	return quad_tree(grid, 0, len(grid)-1, 0, len(grid)-1)
}

func main() {
	grid := [][]int{{1, 1, 1, 1, 0, 0, 0, 0}, {1, 1, 1, 1, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 0, 0, 0, 0}, {1, 1, 1, 1, 0, 0, 0, 0}, {1, 1, 1, 1, 0, 0, 0, 0}, {1, 1, 1, 1, 0, 0, 0, 0}}

	fmt.Println(construct(grid))
}
