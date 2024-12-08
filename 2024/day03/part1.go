package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening input:", err)
		return
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)

	re := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)

	total := 0

	for scanner.Scan() {
		line := scanner.Text()
		matches := re.FindAllStringSubmatch(line, -1)

		for _, match := range matches {
			x, _ := strconv.Atoi(match[1])
			y, _ := strconv.Atoi(match[2])
			total += x * y
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	fmt.Printf("Sum of all multiplication results: %d\n", total)
}
