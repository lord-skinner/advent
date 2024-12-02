package main

import (
	"fmt"
	"os"
)

func main() {
	// Read the file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

}
