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

	// Iterate over the strings
	scanner := bufio.NewScanner(file)
	var charsCode int
	var charsMem int
	var charsDiff int
	var charsNew int
	var charsDiffTwo int
	for scanner.Scan() {
		str := scanner.Text()
		charsCode = len(str)
		charsMem = 0
		charsNew = 0
		i := 0
		for i < charsCode {
			c1 := string(str[i])
			switch c1 {
			case "\"":
				// " --> "\"
				charsNew += 3
				i++
			case "\\":
				c2 := string(str[i+1])
				// Next char is either ", \ or xdd where d is any digit
				if c2 == "\"" || c2 == "\\" {
					charsMem++
					// \" --> \\\", \\ --> \\\\
					charsNew += 4
					i += 2
				} else {
					charsMem++
					// \xdd --> \\xdd
					charsNew += 5
					i += 4
				}
			default:
				charsMem++
				charsNew++
				i++
			}
		}
		charsDiff += charsCode - charsMem
		charsDiffTwo += charsNew - charsCode
	}
	must(file.Close())

	// Part One: The total difference between chars in code strings and chars in memory
	fmt.Printf("Part One: %d\n", charsDiff)

	// Part Two: The total difference between chars in new strings and chars in original strings
	fmt.Printf("Part Two: %d\n", charsDiffTwo)
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
