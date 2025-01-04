package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func must(err error) {
	if err != nil {
		panic(err)
	}
}

func min(nums ...int) int {
	m := nums[0]
	for _, n := range nums[1:] {
		if n < m {
			m = n
		}
	}
	return m
}

func main() {
	// Read input as list of strings
	file, err := os.Open("2015/02/02-input.txt")
	if err != nil {
		panic(err)
	}

	var wrap, ribbon int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// Parse dimensions
		dims := make([]int, 3)
		for i, dim := range strings.Split(scanner.Text(), "x") {
			dims[i], _ = strconv.Atoi(dim)
		}
		l, w, h := dims[0], dims[1], dims[2]

		// Calculate wrapping paper
		wrap += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

		// Calculate ribbon
		sort.Ints(dims)
		ribbon += 2*dims[0] + 2*dims[1] + l*w*h
	}
	defer must(file.Close())

	// Part One: Total square feet of wrapping paper
	fmt.Printf("Part One: %d\n", wrap)

	// Part Two: Total feet of ribbon
	fmt.Printf("Part Two: %d\n", ribbon)
}
