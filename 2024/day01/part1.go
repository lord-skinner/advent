package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer input.Close()

	var col1, col2 []int
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		if len(parts) != 2 {
			fmt.Println("Invalid line:", scanner.Text())
			continue
		}
		v1, _ := strconv.Atoi(parts[0])
		v2, _ := strconv.Atoi(parts[1])
		col1 = append(col1, v1)
		col2 = append(col2, v2)
	}

	// Sort each column independently
	sort.Ints(col1)
	sort.Ints(col2)

	// Calculate absolute differences and sum
	totalDifference := 0
	for i := 0; i < len(col1); i++ {
		diff := int(math.Abs(float64(col1[i] - col2[i])))
		totalDifference += diff
	}

	// Write sorted data and total difference to file
	part1File, err := os.Create("part1.txt")
	if err != nil {
		fmt.Println("Error creating part1 file:", err)
		return
	}
	defer part1File.Close()

	writer := bufio.NewWriter(part1File)
	for i := 0; i < len(col1); i++ {
		fmt.Fprintf(writer, "%d %d\n", col1[i], col2[i])
	}
	fmt.Fprintf(writer, "\nTotal absolute difference: %d\n", totalDifference)
	writer.Flush()

	fmt.Printf("Sorting complete. Results and total difference (%d) written to part1.txt\n", totalDifference)
}
