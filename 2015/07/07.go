package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("2015/07/07-input.txt")
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	var wireValues map[string]int
	var queue [][]string
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		queue = append(queue, parts)
	}
	for len(queue) > 0 {
		for _, q := range queue {
			params := len(q)
			switch params {
			case 3:
				i, _ := strconv.Atoi(q[0])
				wireValues[q[2]] = i
			case 4:
				fmt.Println(wireValues[q[3]])
			}
		}
	}
	must(file.Close())
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
