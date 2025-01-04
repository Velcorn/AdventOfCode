package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"os"
	"strconv"
)

func getMD5Hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func main() {
	// Read input as string
	data, err := os.ReadFile("2015/04/04-input.txt")
	if err != nil {
		panic(err)
	}
	secretKey := string(data)

	var hash string
	var partOne int
	var partTwo int
	i := 0
	condition := true
	first := true
	for condition {
		i++
		hash = getMD5Hash(secretKey + strconv.Itoa(i))
		if hash[0:5] == "00000" && first {
			partOne = i
			first = false
		}
		if hash[0:6] == "000000" {
			partTwo = i
			condition = false
		}
	}

	// Part One: The lowest positive integer that produces an MD5 hash with five leading zeros
	fmt.Printf("Part One: %d\n", partOne)

	// Part Two: The lowest positive integer that produces an MD5 hash with six leading zeros
	fmt.Printf("Part Two: %d\n", partTwo)
}
