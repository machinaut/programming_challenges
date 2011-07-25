// Gattaca (weighted interval scheduling)
// http://www.facebook.com/careers/puzzles.php?puzzle_id=15
// Alex Ray (2011) <ajray@ncsu.edu>
// Dynamic Programming Solution
// TODO(ajray): well a note really... no error checking; feed it good input
// REF: http://www.kelvinjiang.com/2010/10/facebook-puzzles-gattaca.html
package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Gene represents a single gene prediction (3-tuple)
type Gene struct {
	start,stop,score int
}

// NewGene takes a read line of input and returns a new gene
func NewGene(line []byte) Gene {
	fields := strings.Fields(string(line))
	start, _ := strconv.Atoi(fields[0])
	stop, _ := strconv.Atoi(fields[1])
	score, _ := strconv.Atoi(fields[2])
	return Gene{start,stop,score}
}

// Genes is our list of genes, sorted by increasing stop index
var Genes []Gene

func main() {
	flag.Parse()
	if flag.NArg() != 1 {
		fmt.Println("Usage: ./gattaca <inputfile>")
		os.Exit(1)
	}
	infile, _ := os.Open(flag.Arg(0))
	inbuf := bufio.NewReader(infile)
	line,_,_ := inbuf.ReadLine()
	n, _ := strconv.Atoi(string(line))
	// read in
	for i := 0 ; i < n ; i += 80 {
		_,_,_ = inbuf.ReadLine()
	}
	line,_,_ = inbuf.ReadLine()
	n, _ = strconv.Atoi(string(line))
	Genes = make([]Gene,n)
	// read in subsequences
	line,_,_ = inbuf.ReadLine()
	Genes[0] = NewGene(line)
	for j := 1 ; j < n ; j++ {
		line,_,_ = inbuf.ReadLine()
		gene := NewGene(line)
		// insert into Genes sorted by increasing stop index
		var i int
		for i = j - 1 ; i >= 0 && Genes[i].stop > gene.stop ; i-- {
			Genes[i+1] = Genes[i]
		}
		Genes[i+1] = gene
	}
	fmt.Println(Maximum(Genes)[len(Genes)])
}

// Compatable returns an array compatible such that compatible[i] is the
// largest index in the sort order that does not conflict with the ith Gene
func Compatible(A []Gene) (compatible []int) {
	compatible = make([]int,len(A))
	for i := 0 ; i < len(compatible) ; i++ {
		compatible[i] = -1
		for j := i - 1 ; j >= 0 ; j-- {
			if A[j].stop < A[i].start {
				compatible[i] = j
				break
			}
		}
	}
	return compatible
}

// Maximum returns an array maximum such that maximum[i] is the value of the
// best possible subset of (non-overlapping) Genes [0:i] (inclusive)
func Maximum(A []Gene) (maximum []int) {
	maximum = make([]int,len(A)+1)
	compatible := Compatible(A)
	maximum[0] = 0
	for i := 1 ; i < len(maximum) ; i++ {
		include := A[i-1].score + maximum[compatible[i-1]+1]
		exclude := maximum[i-1]
		if include > exclude {
			maximum[i] = include
		} else {
			maximum[i] = exclude
		}
	}
	return maximum
}

