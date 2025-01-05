package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("2015/05/05-input.txt")
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	nice := 0
	niceTwo := 0
	for scanner.Scan() {
		str := scanner.Text()
		if isNice(str) {
			nice++
		}
		if isNiceTwo(str) {
			niceTwo++
		}
	}
	defer must(file.Close())

	// Part One: The number of strings that are nice
	fmt.Printf("Part One: %d\n", nice)

	// Part Two: The number of strings that are nice two
	fmt.Printf("Part Two: %d\n", niceTwo)
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}

func isNice(str string) bool {
	vowels := 0
	twice := false
	substrings := false
	vowelSet := "aeiou"
	forbidden := []string{"ab", "cd", "pq", "xy"}

	for i := 0; i < len(str); i++ {
		// Check if current character is a vowel
		if strings.ContainsRune(vowelSet, rune(str[i])) {
			vowels++
		}

		// Check for repeated characters or forbidden substrings
		if i < len(str)-1 {
			if str[i] == str[i+1] {
				twice = true
			}
			pair := str[i : i+2]
			for _, forbid := range forbidden {
				if pair == forbid {
					substrings = true
					break
				}
			}
		}

		// Early exit if forbidden substring is found
		if substrings {
			return false
		}
	}

	return vowels >= 3 && twice
}

func isNiceTwo(str string) bool {
	twice := false
	repeat := false
	pairs := map[string]int{} // Tracks the last index of each pair

	for i := 0; i < len(str); i++ {
		// Check for repeated character with a gap of one
		if i < len(str)-2 && str[i] == str[i+2] {
			repeat = true
		}

		// Check for a pair appearing twice without overlap
		if i < len(str)-1 {
			pair := str[i : i+2]
			if prevIdx, exists := pairs[pair]; exists && i-prevIdx > 1 {
				twice = true
			} else {
				pairs[pair] = i
			}
		}

		// Early exit if both conditions are satisfied
		if twice && repeat {
			return true
		}
	}

	return false
}
