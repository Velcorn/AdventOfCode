package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Read the input file
	file, err := os.Open("2015/09/09-input.txt")
	if err != nil {
		panic(err)
	}

	// Create the graph
	graph := NewGraph()

	// Iterate over the lines and add nodes and edges to the graph
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		city1, city2, stringDistance := parts[0], parts[2], parts[4]
		distance, err := strconv.Atoi(stringDistance)
		if err != nil {
			panic(err)
		}
		graph.AddEdge(city1, city2, distance)
	}
	must(file.Close())

	// Part One/Two: The distance of the shortest/longest route, visiting all cities
	shortest, longest := heldKarp(graph)
	fmt.Printf("Part One: %d\n", shortest)
	fmt.Printf("Part Two: %d\n", longest)
}

// Graph defines the graph structure
type Graph struct {
	Nodes map[string]map[string]int
}

// NewGraph creates a new graph
func NewGraph() *Graph {
	return &Graph{Nodes: make(map[string]map[string]int)}
}

// AddNode adds a node (city) to the graph
func (g *Graph) AddNode(city string) {
	if _, exists := g.Nodes[city]; !exists {
		g.Nodes[city] = make(map[string]int)
	}
}

// AddEdge adds an edge (connection with distance) between two cities
func (g *Graph) AddEdge(city1, city2 string, distance int) {
	g.AddNode(city1)
	g.AddNode(city2)
	g.Nodes[city1][city2] = distance
	g.Nodes[city2][city1] = distance
}

// heldKarp solves the TSP for both shortest and longest paths
func heldKarp(graph *Graph) (int, int) {
	// Map cities to indices
	cities := make([]string, 0, len(graph.Nodes))
	cityIndex := make(map[string]int)
	for city := range graph.Nodes {
		cityIndex[city] = len(cities)
		cities = append(cities, city)
	}

	n := len(cities)
	inf := math.MaxInt
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			if d, ok := graph.Nodes[cities[i]][cities[j]]; ok {
				dist[i][j] = d
			} else {
				dist[i][j] = inf
			}
		}
	}

	// Memoization for shortest and longest distances
	meMin := make([][]int, 1<<n)
	meMax := make([][]int, 1<<n)
	for i := range meMin {
		meMin[i] = make([]int, n)
		meMax[i] = make([]int, n)
		for j := range meMin[i] {
			meMin[i][j] = inf
			meMax[i][j] = 0
		}
	}

	// Base case: starting at each city
	for i := 0; i < n; i++ {
		meMin[1<<i][i] = 0
		meMax[1<<i][i] = 0
	}

	// State transition
	for mask := 1; mask < (1 << n); mask++ {
		for i := 0; i < n; i++ {
			if mask&(1<<i) == 0 {
				continue
			}
			for j := 0; j < n; j++ {
				if mask&(1<<j) != 0 || dist[i][j] == inf {
					continue
				}
				newMask := mask | (1 << j)
				meMin[newMask][j] = min(meMin[newMask][j], meMin[mask][i]+dist[i][j])
				meMax[newMask][j] = max(meMax[newMask][j], meMax[mask][i]+dist[i][j])
			}
		}
	}

	// Extract shortest and longest tours
	shortest, longest := inf, 0
	finalMask := (1 << n) - 1
	for i := 0; i < n; i++ {
		shortest = min(shortest, meMin[finalMask][i])
		longest = max(longest, meMax[finalMask][i])
	}
	return shortest, longest
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
