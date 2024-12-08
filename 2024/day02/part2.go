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

	increasing := numbers[1] > numbers[0]

	for i := 1; i < len(numbers); i++ {
		diff := numbers[i] - numbers[i-1]
		if (increasing && (diff <= 0 || diff > 3)) ||
			(!increasing && (diff >= 0 || diff < -3)) {
			return false
		}
	}
	return true
}

func canBeMadeSafe(numbers []int) bool {
	for i := range numbers {
		temp := make([]int, len(numbers))
		copy(temp, numbers)
		temp = append(temp[:i], temp[i+1:]...)
		if checkSequence(temp) {
			return true
		}
	}
	return false
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)
	safeCount := 0
	totalCount := 0

	for scanner.Scan() {
		line := scanner.Text()
		numbers := []int{}
		for _, numStr := range strings.Fields(line) {
			num, _ := strconv.Atoi(numStr)
			numbers = append(numbers, num)
		}

		if checkSequence(numbers) || canBeMadeSafe(numbers) {
			safeCount++
		}
		totalCount++
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Printf("Number of safe sequences: %d\n", safeCount)
	fmt.Printf("Total number of sequences: %d\n", totalCount)
}
