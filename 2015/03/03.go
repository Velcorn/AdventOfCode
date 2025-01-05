package main

import (
	"fmt"
	"os"
)

func main() {
	data, err := os.ReadFile("2015/03/03-input.txt")
	if err != nil {
		panic(err)
	}
	directions := string(data)

	moves := map[rune][2]int{
		'^': {0, 1},
		'v': {0, -1},
		'<': {-1, 0},
		'>': {1, 0},
	}

	// Part One: The number of houses that receive at least one present from Santa
	houses := 1
	pos := [2]int{0, 0}
	visited := map[[2]int]bool{pos: true}
	for _, direction := range directions {
		move := moves[direction]
		pos[0] += move[0]
		pos[1] += move[1]
		if !visited[pos] {
			visited[pos] = true
			houses++
		}
	}
	fmt.Printf("Part One: %d\n", houses)

	// Part Two: The number of houses that receive at least one present from (Robo-)Santa
	houses = 1
	sPos, rPos := [2]int{0, 0}, [2]int{0, 0}
	visited = map[[2]int]bool{{0, 0}: true}
	for i, direction := range directions {
		move := moves[direction]
		if i%2 == 0 {
			sPos[0] += move[0]
			sPos[1] += move[1]
			pos = sPos
		} else {
			rPos[0] += move[0]
			rPos[1] += move[1]
			pos = rPos
		}
		if !visited[pos] {
			visited[pos] = true
			houses++
		}
	}
	fmt.Printf("Part Two: %d\n", houses)
}
