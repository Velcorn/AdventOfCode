package main

import (
	"fmt"
	"os"
)

func main() {
	file, err := os.ReadFile("2015/01/01-input.txt")
	if err != nil {
		panic(err)
	}
	directions := string(file)

	// Count the number of open and close parentheses
	var floor int
	var basement int
	for i, direction := range directions {
		if direction == '(' {
			floor++
		} else {
			floor--
			// Track the first time direction leads to basement
			if floor == -1 && basement == 0 {
				basement = i + 1
			}
		}
	}

	// Part One: The floor Santa ends up on
	fmt.Printf("Part One: %d\n", floor)

	// Part Two: The position of the character that causes Santa to first enter the basement
	fmt.Printf("Part Two: %d\n", basement)
}
