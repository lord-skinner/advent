package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	grid := readInput("input.txt")

	count := countXMAS(grid)

	fmt.Printf("XMAS appears %d times in the word search.\n", count)
}

func readInput(filename string) [][]rune {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var grid [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		grid = append(grid, []rune(scanner.Text()))
	}

	return grid
}

func countXMAS(grid [][]rune) int {
	count := 0
	rows, cols := len(grid), len(grid[0])
	directions := [][]int{{0, 1}, {1, 0}, {1, 1}, {1, -1}, {0, -1}, {-1, 0}, {-1, -1}, {-1, 1}}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			for _, dir := range directions {
				if checkXMAS(grid, i, j, dir[0], dir[1]) {
					count++
				}
			}
		}
	}

	return count
}

func checkXMAS(grid [][]rune, row, col, dx, dy int) bool {
	rows, cols := len(grid), len(grid[0])
	xmas := []rune{'X', 'M', 'A', 'S'}

	for k := 0; k < 4; k++ {
		x, y := row+k*dx, col+k*dy
		if x < 0 || x >= rows || y < 0 || y >= cols || grid[x][y] != xmas[k] {
			return false
		}
	}

	return true
}
