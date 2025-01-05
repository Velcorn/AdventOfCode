package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("2015/06/06-input.txt")
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	var grid [1000][1000]bool
	var grid2 [1000][1000]int
	for scanner.Scan() {
		line := scanner.Text()
		op, x1, y1, x2, y2 := parseOperation(line)
		for x := x1; x <= x2; x++ {
			for y := y1; y <= y2; y++ {
				switch op {
				case "on":
					grid[x][y] = true
					grid2[x][y]++
				case "off":
					grid[x][y] = false
					if grid2[x][y] > 0 {
						grid2[x][y]--
					}
				case "toggle":
					grid[x][y] = !grid[x][y]
					grid2[x][y] += 2
				}
			}
		}
	}
	defer must(file.Close())

	lights := 0
	brightness := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			if grid[x][y] {
				lights++
			}
			brightness += grid2[x][y]
		}
	}

	// Part One: The number of lights that are lit
	fmt.Printf("Part One: %d\n", lights)

	// Part Two: The total brightness of all lights
	fmt.Printf("Part One: %d\n", brightness)
}

func parseOperation(line string) (string, int, int, int, int) {
	parts := strings.Fields(line)
	var op string
	var x1, y1, x2, y2 int

	if parts[0] == "toggle" {
		op = "toggle"
		x1, y1 = parseCoordinates(parts[1])
		x2, y2 = parseCoordinates(parts[3])
	} else {
		op = parts[1] // "on" or "off"
		x1, y1 = parseCoordinates(parts[2])
		x2, y2 = parseCoordinates(parts[4])
	}
	return op, x1, y1, x2, y2
}

func parseCoordinates(coord string) (int, int) {
	parts := strings.Split(coord, ",")
	x, _ := strconv.Atoi(parts[0])
	y, _ := strconv.Atoi(parts[1])
	return x, y
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
