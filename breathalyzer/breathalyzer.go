// Breathalyzer
// http://www.facebook.com/careers/puzzles.php?puzzle_id=17
// Alex Ray (2011) <ajray@ncsu.edu>
package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
)

func main() {
	// first half is just reading the file
	flag.Parse()
	if flag.NArg() != 1 {
		fmt.Println("Usage: ./breathalyzer <inputfile>")
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
	fmt.Println(string(line))
}
