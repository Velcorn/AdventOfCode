package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Read the input file
	file, err := os.Open("2015/07/07-input.txt")
	if err != nil {
		panic(err)
	}

	// Parse the instructions into a queue
	scanner := bufio.NewScanner(file)
	var instructions [][]string
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		instructions = append(instructions, parts)
	}
	must(file.Close())

	// Part One: Get the signal for wire "a"
	partOne := simulateCircuit(instructions, nil)
	fmt.Printf("Part One: %d\n", partOne)

	// Part Two: Override wire "b" with the signal from Part One and reset the circuit
	partTwo := simulateCircuit(instructions, &partOne)
	fmt.Printf("Part Two: %d\n", partTwo)
}

// simulateCircuit simulates the circuit and returns the signal for wire "a".
func simulateCircuit(instructions [][]string, overrideB *uint16) uint16 {
	wireValues := map[string]uint16{}
	queue := append([][]string{}, instructions...)

	for len(queue) > 0 {
		q := queue[0]
		queue = queue[1:]

		switch len(q) {
		case 3: // "123 -> x" or "a -> x"
			value, err := strconv.Atoi(q[0])
			if err != nil {
				// Value is another wire
				if val, exists := wireValues[q[0]]; exists {
					wireValues[q[2]] = val
				} else {
					// Retry later if the value is not ready
					queue = append(queue, q)
				}
			} else {
				// Value is a constant
				if q[2] == "b" && overrideB != nil {
					// Override wire "b" for Part Two
					wireValues[q[2]] = *overrideB
				} else {
					wireValues[q[2]] = uint16(value)
				}
			}

		case 4: // "NOT x -> h"
			if val, exists := wireValues[q[1]]; exists {
				wireValues[q[3]] = ^val
			} else {
				queue = append(queue, q)
			}

		case 5: // "x AND y -> d", "x OR y -> e", etc.
			i1, i2 := getValue(wireValues, q[0]), getValue(wireValues, q[2])
			if i1 != nil && i2 != nil {
				switch q[1] {
				case "AND":
					wireValues[q[4]] = *i1 & *i2
				case "OR":
					wireValues[q[4]] = *i1 | *i2
				case "LSHIFT":
					wireValues[q[4]] = *i1 << *i2
				case "RSHIFT":
					wireValues[q[4]] = *i1 >> *i2
				}
			} else {
				queue = append(queue, q)
			}
		}
	}

	return wireValues["a"]
}

// getValue checks if a string is a number or a wire and returns its value.
func getValue(wireValues map[string]uint16, input string) *uint16 {
	value, err := strconv.Atoi(input)
	if err != nil {
		// Input is a wire
		if val, exists := wireValues[input]; exists {
			temp := val
			return &temp
		}
		return nil
	}
	// Input is a number
	val := uint16(value)
	return &val
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
