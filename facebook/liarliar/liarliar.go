// Liar, Liar
// Yup, its just a bipartite graph
// http://www.facebook.com/careers/puzzles.php?puzzle_id=20
// Alex Ray (2011) <ajray@ncsu.edu>
//
// TODO(ajray):
// * Handle arbitrarily large names
// * Add line numbers to error output
// * Make each error string unique (for grep-ing) and useful
// * Error string reports what infile is wrong, not what parsing failed
// * sanity check: all people eventually end up in A or B
// * sanity check: no one ends up in both A and B
package main

import (
	"bufio"
	"fmt"
	"flag"
	"os"
	"strconv"
	"strings"
)

type List map[string]bool
type Digraph map[string] List

func (d Digraph) String() (s string) {
	s += fmt.Sprintf("%d",len(d))
	for name, nameList := range d {
		s += fmt.Sprintf("\n%s %d",name,len(nameList))
		for name, _ := range nameList {
			s += "\n" + name
		}
	}
	return s
}
func (d Digraph) del(name string) {
	d[name] = nil, false
}
func (l List) has(name string) bool {
	_, ok := l[name]
	return ok
}
func (l List) hasList(list List) bool {
	for name, _ := range list {
		if l.has(name) {
			return true
		}
	}
	return false
}
func (l List) add(name string) {
	l[name] = true
}
func (l List) addList(list List) {
	for name, _ := range list {
		l[name] = true
	}
}

// read input file into a Digraph structure
// TODO(ajray): put line numbers in error output
func readAccusers(inputfilename string) (accusers Digraph, err os.Error) {
	infile, err := os.Open(inputfilename)
	if err != nil {
		return nil, fmt.Errorf("Error opening file: %s", err.String())
	}
	bufrd := bufio.NewReader(infile)
	line,_,err := bufrd.ReadLine()
	// TODO(ajray): account for not reading the whole number
	if err != nil {
		return nil, fmt.Errorf("Error reading file: %s", err.String())
	}
	numAccusers, err := strconv.Atoi(string(line))
	if err != nil {
		return nil, fmt.Errorf("Error reading count: %s", err.String())
	}
	accusers = Digraph(make(map[string] List))
	// now we start reading the input file
	for j := 0 ; j < numAccusers ; j++ {
		line,_,err := bufrd.ReadLine()
		// TODO(ajray): account for not reading the whole number
		if err != nil {
			return nil, fmt.Errorf("Error reading file: %s", err.String())
		}
		fields := strings.Fields(string(line))
		if len(fields) != 2 {
			return nil, fmt.Errorf("Error reading accuser %d, got %d fields(expected 2); Line: %s",
				j, len(fields), string(line))
		}
		accuser := fields[0]
		numAccused, err := strconv.Atoi(fields[1])
		if err != nil {
			return nil, fmt.Errorf("Error reading count for accuser %d(%s): %s ; Line: %s",
				j, accuser, err.String(), string(line))
		}
		if list, ok := accusers[accuser]; !ok || list == nil {
			accusers[accuser] = List(make(map[string] bool))
		}
		for i := 0 ; i < numAccused ; i++ {
			line,_,err := bufrd.ReadLine()
			// TODO(ajray): account for not reading the whole line
			if err != nil {
				return nil, fmt.Errorf("Error reading file at accuser %d(%s) accused %d: %s",
					j, accuser, i, err.String())
			}
			fields = strings.Fields(string(line))
			if len(fields) != 1 {
				return nil, fmt.Errorf("Error reading file at accuser %d(%s) accused %d," +
					" got %d fields (expected 1); Line: %s",
					j, accuser, i, len(fields), string(line))
			}
			accused := fields[0]
			accusers[accuser][accused] = true
		}
	}
	return accusers, nil
}

func main() {
	// check commandline argument (just one, the filename)
	flag.Parse()
	if flag.NArg() != 1 {
		fmt.Println("Usage: ./liarliar <inputfile>")
		os.Exit(1)
	}
	// parse this input into a Digraph
	accusers, err := readAccusers(flag.Arg(0))
	if err != nil {
		fmt.Println("Error failed to read file:", err)
		os.Exit(1)
	}
	//fmt.Println(accusers)
	aList := List(make(map[string] bool))
	bList := List(make(map[string] bool))
	for len(accusers) > 0 {
		// loop until accusers is exhausted
		for accuser, accuserList := range accusers {
			if aList.has(accuser) { // accuser in A
				bList.addList(accuserList)
				accusers.del(accuser)
			} else if bList.has(accuser) { // accuser in B
				aList.addList(accuserList)
				accusers.del(accuser)
			} else if aList.hasList(accuserList) { // accused in A
				bList.add(accuser)
				aList.addList(accuserList)
				accusers.del(accuser)
			} else if bList.hasList(accuserList) { // accused in B
				aList.add(accuser)
				bList.addList(accuserList)
				accusers.del(accuser)
			} else if len(aList) == 0 && len(bList) == 0 { // init
				aList.add(accuser)
				bList.addList(accuserList)
				accusers.del(accuser)
			}
		}
	}
	//fmt.Println(aList)
	//fmt.Println(bList)
	aLen := len(aList)
	bLen := len(bList)
	if aLen > bLen {
		fmt.Printf("%d %d\n", aLen, bLen)
	} else {
		fmt.Printf("%d %d\n", bLen, aLen)
	}
}
