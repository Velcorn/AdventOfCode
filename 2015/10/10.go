package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	// Read the input file as a single string
	data, err := os.ReadFile("2015/10/10-input.txt")
	if err != nil {
		panic(err)
	}
	sequence := string(data)

	// Part One: The length of the resulting sequence after 40 iterations
	length := lookAndSay(sequence, 40)
	fmt.Printf("Part One: %d\n", length)

	// Part Two: The length of the resulting sequence after 50 iterations
	length = lookAndSay(sequence, 50)
	fmt.Printf("Part Two: %d\n", length)
}

// lookAndSay recursively generates the Look-and-Say sequence for a given number of iterations and returns its length.
func lookAndSay(sequence string, iterations int) int {
	if iterations == 0 {
		return len(sequence)
	}

	// Generate the next sequence
	var next strings.Builder
	count := 1
	for i := 1; i < len(sequence); i++ {
		if sequence[i] == sequence[i-1] {
			count++
		} else {
			next.WriteString(fmt.Sprintf("%d%c", count, sequence[i-1]))
			count = 1
		}
	}
	// Append the last group
	next.WriteString(fmt.Sprintf("%d%c", count, sequence[len(sequence)-1]))

	// Recur for the next iteration
	return lookAndSay(next.String(), iterations-1)
}
