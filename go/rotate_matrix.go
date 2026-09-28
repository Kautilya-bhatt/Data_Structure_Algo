package main

import "fmt"

// rotate90 rotates an n×n matrix 90 degrees clockwise in place.
func rotate90(matrix [][]int) {
    n := len(matrix)
    for layer := 0; layer < n/2; layer++ {
        first := layer
        last := n - 1 - layer
        for i := first; i < last; i++ {
            offset := i - first
            top := matrix[first][i]
            // left -> top
            matrix[first][i] = matrix[last-offset][first]
            // bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            // right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            // top -> right
            matrix[i][last] = top
        }
    }
}

func main() {
    m := [][]int{{1,2,3},{4,5,6},{7,8,9}}
    fmt.Println("Before:", m)
    rotate90(m)
    fmt.Println("After:", m)
}
