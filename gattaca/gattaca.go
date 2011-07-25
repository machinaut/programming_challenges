// Gattaca
// http://www.facebook.com/careers/puzzles.php?puzzle_id=15
// Alex Ray (2011) <ajray@ncsu.edu>
package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// TODO(ajray):
//	Line numbers in error output
//	Errors describe problem in input file, not the parsing error

// Gene represents a single gene prediction (3-tuple)
type Gene struct {
	start,stop,score int
}

var Genes = make([]Gene,0) // will grow

func main() {
	flag.Parse()
	if flag.NArg() != 1 {
		fmt.Println("Usage: ./gattaca <inputfile>")
		os.Exit(1)
	}
	infile, err := os.Open(flag.Arg(0))
	if err != nil {
		fmt.Println("Error opening input file:", err)
		os.Exit(1)
	}
	inbuf := bufio.NewReader(infile)
	line,_,err := inbuf.ReadLine()
	// TODO(ajray): account for not reading the whole line
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}
	n, err := strconv.Atoi(string(line))
	if err != nil {
		fmt.Println("Error reading count:", err)
		os.Exit(1)
	}
	// read in
	//genome := ""
	for i := 0 ; i < n ; i += 80 {
		// TODO(ajray): account for not reading the whole line
		_,_,err := inbuf.ReadLine()
		// TODO(ajray): handle errors
		if err != nil { // assume its os.EOF
			fmt.Println("Error reading line:", err)
			os.Exit(1)
		}
		//genome += strings.TrimSpace(string(line))
	}
	line,_,err = inbuf.ReadLine()
	// TODO(ajray): account for not reading the whole line
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}
	n, err = strconv.Atoi(string(line))
	if err != nil {
		fmt.Println("Error reading count:", err)
		os.Exit(1)
	}
	// read in subsequences
	for i := 0 ; i < n ; i++ {
		// TODO(ajray): account for not reading the whole line
		line,_,err := inbuf.ReadLine()
		// TODO(ajray): handle errors
		if err != nil { // assume its os.EOF
			fmt.Println("Error reading line:", err)
			os.Exit(1)
		}
		fields := strings.Fields(string(line))
		if len(fields) != 3 {
			fmt.Println("Error reading Gene:", fields)
			os.Exit(1)
		}
		start, err := strconv.Atoi(fields[0])
		if err != nil {
			fmt.Println("Error reading start:", err)
			os.Exit(1)
		}
		stop, err := strconv.Atoi(fields[1])
		if err != nil {
			fmt.Println("Error reading stop:", err)
			os.Exit(1)
		}
		score, err := strconv.Atoi(fields[2])
		if err != nil {
			fmt.Println("Error reading score:", err)
			os.Exit(1)
		}
		Genes = append(Genes, Gene{start,stop,score})
	}
	fmt.Println(Genes)
}

// Overlap checks if two Genes overlap
func Overlap(a, b Gene) bool {
	return a.stop < b.start || b.stop <= a.start
}
