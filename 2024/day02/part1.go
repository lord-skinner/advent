package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func checkSequence(numbers []int) bool {
	if len(numbers) < 2 {
		return true
	}

	diff := numbers[1] - numbers[0]
	increasing := diff > 0

	for i := 1; i < len(numbers); i++ {
		currentDiff := numbers[i] - numbers[i-1]
		if (increasing && (currentDiff <= 0 || currentDiff > 3)) ||
			(!increasing && (currentDiff >= 0 || currentDiff < -3)) {
			return false
		}
	}
	return true
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	safeCount := 0
	totalCount := 0

	for scanner.Scan() {
		line := scanner.Text()
		numbers := []int{}
		for _, numStr := range strings.Fields(line) {
			num, _ := strconv.Atoi(numStr)
			numbers = append(numbers, num)
		}

		if checkSequence(numbers) {
			safeCount++
		}
		totalCount++
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Printf("Number of safe reports: %d\n", safeCount)
	fmt.Printf("Total number of reports: %d\n", totalCount)
}
