package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	input := string(content)

	rules, updates := parseInput(input)

	// Part One
	resultPart1 := calculateResultPart1(updates, rules)
	fmt.Println("Part One - Sum of middle page numbers for correct updates:", resultPart1)

	// Part Two
	resultPart2 := calculateResultPart2(updates, rules)
	fmt.Println("Part Two - Sum of middle page numbers for corrected updates:", resultPart2)
}

func parseInput(input string) (map[int][]int, [][]int) {
	parts := strings.Split(input, "\n\n")
	ruleLines := strings.Split(parts[0], "\n")
	updateLines := strings.Split(parts[1], "\n")

	rules := make(map[int][]int)
	for _, line := range ruleLines {
		if line == "" {
			continue
		}
		nums := strings.Split(line, "|")
		x := parseInt(nums[0])
		y := parseInt(nums[1])
		rules[x] = append(rules[x], y)
	}

	var updates [][]int
	for _, line := range updateLines {
		if line == "" {
			continue
		}
		var update []int
		for _, num := range strings.Split(line, ",") {
			update = append(update, parseInt(num))
		}
		updates = append(updates, update)
	}

	return rules, updates
}

func parseInt(s string) int {
	num, _ := strconv.Atoi(strings.TrimSpace(s))
	return num
}

func isCorrectOrder(update []int, rules map[int][]int) bool {
	seen := make(map[int]bool)
	for _, page := range update {
		seen[page] = true
		for _, after := range rules[page] {
			if seen[after] {
				return false
			}
		}
	}
	return true
}

func calculateResultPart1(updates [][]int, rules map[int][]int) int {
	sum := 0
	for _, update := range updates {
		if isCorrectOrder(update, rules) {
			middleIndex := len(update) / 2
			sum += update[middleIndex]
		}
	}
	return sum
}

func calculateResultPart2(updates [][]int, rules map[int][]int) int {
	sum := 0
	for _, update := range updates {
		if !isCorrectOrder(update, rules) {
			sortedUpdate := topologicalSort(update, rules)
			middleIndex := len(sortedUpdate) / 2
			sum += sortedUpdate[middleIndex]
		}
	}
	return sum
}

func topologicalSort(pages []int, rules map[int][]int) []int {
	graph := make(map[int][]int)
	inDegree := make(map[int]int)
	for _, page := range pages {
		graph[page] = []int{}
		inDegree[page] = 0
	}
	for page, afterPages := range rules {
		for _, afterPage := range afterPages {
			if _, exists := graph[page]; exists && contains(pages, afterPage) {
				graph[page] = append(graph[page], afterPage)
				inDegree[afterPage]++
			}
		}
	}

	var queue []int
	for page := range graph {
		if inDegree[page] == 0 {
			queue = append(queue, page)
		}
	}

	var result []int
	for len(queue) > 0 {
		page := queue[0]
		queue = queue[1:]
		result = append(result, page)
		for _, afterPage := range graph[page] {
			inDegree[afterPage]--
			if inDegree[afterPage] == 0 {
				queue = append(queue, afterPage)
			}
		}
	}

	return result
}

func contains(slice []int, item int) bool {
	for _, v := range slice {
		if v == item {
			return true
		}
	}
	return false
}
