// Hoppity Hop!
// http://www.facebook.com/careers/puzzles.php?puzzle_id=7
// Alex Ray (2011) <ajray@ncsu.edu>
package main

import (
	"bufio"
	"fmt"
	"flag"
	"os"
	"strconv"
)

func main() {
	// first half is just reading the file
	flag.Parse()
	if flag.NArg() != 1 {
		fmt.Println("Usage: ./hoppity <inputfile>")
		os.Exit(1)
	}
	infile, err := os.Open(flag.Arg(0))
	if err != nil {
		fmt.Println("Error opening file:", err)
		os.Exit(1)
	}
	bufrd := bufio.NewReader(infile)
	line,_,err := bufrd.ReadLine()
	// TODO(ajray): account for not reading the whole number
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}
	i, err := strconv.Atoi(string(line))
	if err != nil {
		fmt.Println("Error reading count:", err)
		os.Exit(1)
	}
	// at this point, we've got the number we wanted
	for j := 1 ; j <= i ; j++ {
		switch {
			case j % 15 == 0: fmt.Println("Hop")
			case j % 5 == 0: fmt.Println("Hophop")
			case j % 3 == 0: fmt.Println("Hoppity")
		}
	}
}
