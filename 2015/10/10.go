package main

import (
	"fmt"
	"os"
)

func main() {
	// Read the input file as single string
	data, err := os.ReadFile("2015/10/10-input.txt")
	if err != nil {
		panic(err)
	}
	sequence := string(data)

	// Part One: The length of the resulting sequence after 40 iterations
	lenquence := sequenceLength(sequence, 40)
	fmt.Printf("Part One: %d\n", lenquence)

	// Part Two: The length of the resulting sequence after 50 iterations
	lenquence = sequenceLength(sequence, 50)
	fmt.Printf("Part One: %d\n", lenquence)
}

func sequenceLength(sequence string, iterations int) int {
	// Base case
	if iterations == 0 {
		return len(sequence)
	}

	// Generate the next sequence
	var newSequence string
	count := 1
	char := sequence[0]
	for i := 1; i < len(sequence); i++ {
		if sequence[i] == char {
			count++
		} else {
			newSequence += fmt.Sprintf("%d%c", count, char)
			char = sequence[i]
			count = 1
		}
	}
	// Append the last group
	newSequence += fmt.Sprintf("%d%c", count, char)

	return sequenceLength(newSequence, iterations-1)
}
