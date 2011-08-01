// Meep meep!
// http://www.facebook.com/careers/puzzles.php?puzzle_id=3
// Alex Ray (2011) <ajray@ncsu.edu>
package main

import (
	"fmt"
	"flag"
	"os"
)

func main() {
	// first half is just reading the file
	flag.Parse()
	if flag.NArg() != 1 {
		fmt.Println("Usage: ./hoppity <inputfile>")
		os.Exit(1)
	}
	fmt.Println("Meep meep!")
}
