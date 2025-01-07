package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Read the input file
	file, err := os.Open("2015/08/08-input.txt")
	if err != nil {
		panic(err)
	}

	// Initialize counters
	var charsCode, charsMem, charsNew int

	// Iterate over the strings
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		str := scanner.Text()
		charsCode += len(str)
		charsMem += memorySize(str)
		charsNew += encodedSize(str)
	}
	must(file.Close())

	// Part One: The total difference between chars in code and chars in memory
	fmt.Printf("Part One: %d\n", charsCode-charsMem)

	// Part Two: The total difference between chars in encoded and original strings
	fmt.Printf("Part Two: %d\n", charsNew-charsCode)
}

// memorySize calculates the number of characters in memory representation.
func memorySize(str string) int {
	memSize := 0
	for i := 0; i < len(str); i++ {
		if str[i] == '\\' {
			if str[i+1] == 'x' {
				i += 3 // Skip \xDD
			} else {
				i++ // Skip escaped character
			}
		}
		if str[i] != '"' {
			memSize++
		}
	}
	return memSize
}

// encodedSize calculates the number of characters in encoded representation.
func encodedSize(str string) int {
	encSize := 2 // Account for the added quotes
	for i := 0; i < len(str); i++ {
		if str[i] == '\\' || str[i] == '"' {
			encSize += 2 // Escaped characters add two
		} else {
			encSize++
		}
	}
	return encSize
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
