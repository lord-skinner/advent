package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatalf("Failed to read input file: %v", err)
	}

	result := evaluateCorruptedMemory(string(input))
	fmt.Printf("Sum of enabled multiplications: %d\n", result)
}

func evaluateCorruptedMemory(input string) int {
	sum := 0
	enabled := true
	re := regexp.MustCompile(`(do\(\)|don't\(\)|mul\((\d+),(\d+)\))`)
	matches := re.FindAllStringSubmatch(input, -1)

	for _, match := range matches {
		instruction := match[1]
		switch {
		case instruction == "do()":
			enabled = true
		case instruction == "don't()":
			enabled = false
		case strings.HasPrefix(instruction, "mul("):
			if enabled {
				a, _ := strconv.Atoi(match[2])
				b, _ := strconv.Atoi(match[3])
				sum += a * b
			}
		}
	}

	return sum
}
