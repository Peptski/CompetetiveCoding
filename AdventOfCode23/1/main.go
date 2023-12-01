package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	fmt.Println("Answer to part one: ", solve(false))
	fmt.Println("Answer to part two: ", solve(true))
}

func solve(partTwo bool) int {
	file, _ := os.Open("data")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		line := string(scanner.Text())

		if partTwo {
			line = strings.Replace(line, "one", "o1ne", -1)
			line = strings.Replace(line, "two", "t2wo", -1)
			line = strings.Replace(line, "three", "t3hree", -1)
			line = strings.Replace(line, "four", "f4our", -1)
			line = strings.Replace(line, "five", "f5ive", -1)
			line = strings.Replace(line, "six", "s6ix", -1)
			line = strings.Replace(line, "seven", "s7even", -1)
			line = strings.Replace(line, "eight", "e8ight", -1)
			line = strings.Replace(line, "nine", "n9ine", -1)
		}

		for {
			if !unicode.IsDigit(rune(line[0])) {
				line = line[1:]
			}

			if !unicode.IsDigit(rune(line[len(line)-1])) {
				line = line[:len(line)-1]
			}

			if unicode.IsDigit(rune(line[0])) && unicode.IsDigit(rune(line[len(line)-1])) {
				num, _ := strconv.Atoi(string(line[0]) + string(line[len(line)-1]))
				total += num
				break
			}

		}

	}

	return total
}
