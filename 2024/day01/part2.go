package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// Read the file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var leftList, rightList []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		if len(parts) != 2 {
			fmt.Println("Invalid line:", scanner.Text())
			continue
		}
		left, _ := strconv.Atoi(parts[0])
		right, _ := strconv.Atoi(parts[1])
		leftList = append(leftList, left)
		rightList = append(rightList, right)
	}

	// Sort each list independently
	sort.Ints(leftList)
	sort.Ints(rightList)

	// Count occurrences in the right list
	rightCounts := make(map[int]int)
	for _, num := range rightList {
		rightCounts[num]++
	}

	// Calculate similarity score
	similarityScore := 0
	for _, num := range leftList {
		similarityScore += num * rightCounts[num]
	}

	// Write results to file
	part2File, err := os.Create("part2.txt")
	if err != nil {
		fmt.Println("Error creating part2 file:", err)
		return
	}
	defer part2File.Close()

	writer := bufio.NewWriter(part2File)
	fmt.Fprintf(writer, "Sorted Left List: %v\n", leftList)
	fmt.Fprintf(writer, "Sorted Right List: %v\n", rightList)
	fmt.Fprintf(writer, "Similarity Score: %d\n", similarityScore)
	writer.Flush()

	fmt.Printf("Processing complete. Similarity score: %d. Results written to part2.txt\n", similarityScore)
}
