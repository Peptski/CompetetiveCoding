package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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
	totalPowers := 0

	for scanner.Scan() {
		line := string(scanner.Text())

		valid := true

		minR, minG, minB := 0, 0, 0

		redConstraint, greenConstraint, blueConstraint := 12, 13, 14

		parts := strings.Split(line, ": ")

		sets := strings.Split(parts[1], "; ")

		for _, set := range sets {
			r, g, b := 0, 0, 0
			for _, color := range strings.Split(set, ", ") {
				if strings.Contains(color, "red") {
					num, _ := strconv.Atoi(strings.Replace(color, " red", "", -1))
					r += num
				}
				if strings.Contains(color, "green") {

					num, _ := strconv.Atoi(strings.Replace(color, " green", "", -1))
					g += num
				}
				if strings.Contains(color, "blue") {

					num, _ := strconv.Atoi(strings.Replace(color, " blue", "", -1))
					b += num
				}
			}

			if partTwo {
				if r > minR {
					minR = r
				}
				if g > minG {
					minG = g
				}
				if b > minB {
					minB = b
				}
			}

			if r > redConstraint || g > greenConstraint || b > blueConstraint {
				valid = false
			}

		}

		if partTwo {
			totalPowers += (minR * minG * minB)
		}

		if valid {
			totInc, _ := strconv.Atoi(strings.Replace(parts[0], "Game ", "", -1))
			total += totInc
		}

	}

	if partTwo {
		return totalPowers
	} else {
		return total
	}
}
