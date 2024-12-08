package main

import (
	"bufio"
	"fmt"
	"os"
)

func countXMAS(grid []string) int {
	count := 0
	rows := len(grid)
	cols := len(grid[0])

	for i := 1; i < rows-1; i++ {
		for j := 1; j < cols-1; j++ {
			if isXMAS(grid, i, j) {
				count++
			}
		}
	}

	return count
}

func isXMAS(grid []string, i, j int) bool {
	patterns := []string{"MAS", "SAM"}
	for _, p1 := range patterns {
		for _, p2 := range patterns {
			if (grid[i-1][j-1] == p1[0] && grid[i][j] == p1[1] && grid[i+1][j+1] == p1[2]) &&
				(grid[i-1][j+1] == p2[0] && grid[i][j] == p2[1] && grid[i+1][j-1] == p2[2]) {
				return true
			}
		}
	}
	return false
}

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening input:", err)
		return
	}
	defer input.Close()

	var grid []string
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		grid = append(grid, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	result := countXMAS(grid)
	fmt.Printf("X-MAS appears %d times in the grid\n", result)
}
