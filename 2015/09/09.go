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
	file, err := os.Open("2015/09/09-input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// Create the graph
	graph := NewGraph()

	// Iterate over the lines and add nodes and edges to the graph
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		if len(parts) != 5 {
			panic("Invalid input format")
		}
		city1, city2, stringDistance := parts[0], parts[2], parts[4]
		distance, err := strconv.Atoi(stringDistance)
		if err != nil {
			panic(err)
		}
		graph.AddEdge(city1, city2, distance) // Handles undirected edges
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	// Part One: The distance of the shortest route, visiting all cities
	distances := dijkstra(graph, "Arbre") // Replace "Arbre" with an actual city name in your input
	shortest := -1
	for _, distance := range distances {
		if shortest == -1 || distance < shortest {
			shortest = distance
		}
	}
	fmt.Printf("Part One: %d\n", shortest)
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
	g.Nodes[city2][city1] = distance // Ensure undirected graph
}

// dijkstra calculates the shortest paths from a start node
func dijkstra(graph *Graph, start string) map[string]int {
	distances := make(map[string]int)
	visited := make(map[string]bool)

	// Initialize distances with infinity
	for city := range graph.Nodes {
		distances[city] = 1<<31 - 1 // Max int value
	}
	distances[start] = 0

	for len(visited) < len(graph.Nodes) {
		current := ""
		for city := range graph.Nodes {
			if !visited[city] && (current == "" || distances[city] < distances[current]) {
				current = city
			}
		}
		if current == "" {
			break
		}
		visited[current] = true
		for neighbor, distance := range graph.Nodes[current] {
			newDist := distances[current] + distance
			if newDist < distances[neighbor] {
				distances[neighbor] = newDist
			}
		}
	}
	return distances
}
