// Breathalyzer
// http://www.facebook.com/careers/puzzles.php?puzzle_id=17
// Alex Ray (2011) <ajray@ncsu.edu>
// TODO(ajray):
// * Support Unicode runes, not just ASCII chars
// * Check sorted while reading in
// * Sort unsorted input
// * Error checking on negative score cases
package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strings"
)

const wordfilename = "twl06.txt" // /var/tmp/twl06.txt
const alphabet = "abcdefghijklmnopqrstuvwxyz"

var dict = make([]string, 0) // it'll have to grow

// score a list of words, return the sum of the whole list
func scoreList(words []string) (sum int) {
	sum = 0
	for _, word := range words {
		if score := scoreWord(word) ; score < 0 {
			return -1 // error has occured
		} else {
			sum += score
		}
	}
	return sum
}

// score a word
func scoreWord(word string) (sum int) {
	if findWord(word) != -1 { // found it
		return 0
	}
	list := mutateWord(word)
	for sum = 1 ; true ; sum++ {
		for _, word := range list {
			if findWord(word) != -1 {
				return sum
			}
		}
		list = mutateList(list)
	}
	return -1 // no idea what happens if we get here
}

// look up word in dictionary
func findWord(word string) int {
	//fmt.Printf("Finding %s\n",word)
	min, max := 0, len(dict)
	for min <= max {
		mid := (min + max) / 2
		//fmt.Printf("Checking %d(%s) %d %d\n",mid,dict[mid],min,max)
		if dict[mid] == word {
			return mid
		}
		if word > dict[mid] {
			min = mid + 1
		} else {
			max = mid - 1
		}
	}
	return -1
}

func mutateList(words []string) (list []string) {
	list = make([]string, 0) // will grow
	for _, word := range words {
		list = append(list, mutateWord(word)...)
	}
	return list
}

func mutateWord(word string) (list []string) {
	list = make([]string, 0) // will grow
	list = append(list, replaceWord(word)...)
	list = append(list, insertWord(word)...)
	list = append(list, removeWord(word)...)
	return list
}

func replaceWord(word string) (list []string) {
	list = make([]string, 0) // will grow
	for i := 0 ; i < len(word) ; i++ {
		for _, char := range alphabet {
			newword := []int(word)
			newword[i] = char
			if word != string(newword) {
				list = append(list, string(newword))
			}
		}
	}
	return list
}

func insertWord(word string) (list []string) {
	list = make([]string, 0) // will grow
	for i := 0 ; i < len(word) ; i++ {
		for _, char := range alphabet {
			newword := []int(word[0:i])
			newword = append(newword, char)
			newword = append(newword,[]int(word[i:])...)
			if word != string(newword) {
				list = append(list, string(newword))
			}
		}
	}
	return list
}

func removeWord(word string) (list []string) {
	list = make([]string, 0) // will grow
	for i := 0 ; i < len(word); i++ {
		newword := []int(word[0:i])
		if i < len(word) - 1 {
			newword = append(newword,[]int(word[i+1:])...)
		}
		if word != string(newword) {
			list = append(list, string(newword))
		}
	}
	return list
}


func main() {
	// first half is just reading the file
	flag.Parse()
	if flag.NArg() != 1 {
		fmt.Println("Usage: ./breathalyzer <inputfile>")
		os.Exit(1)
	}
	infile, err := os.Open(flag.Arg(0))
	if err != nil {
		fmt.Println("Error opening input file:", err)
		os.Exit(1)
	}
	inbuf := bufio.NewReader(infile)
	line,_,err := inbuf.ReadLine()
	fields := strings.Fields(strings.ToLower(string(line)))
	// TODO(ajray): account for not reading the whole line
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}
	wordfile, err := os.Open(wordfilename)
	if err != nil {
		fmt.Println("Error opening dictionary file:", err)
		os.Exit(1)
	}
	// read in the dictionary 
	wordbuf := bufio.NewReader(wordfile)
	for {
		// TODO(ajray): account for not reading the whole line
		line,_,err := wordbuf.ReadLine()
		word := strings.TrimSpace(string(line))
		// TODO(ajray): buffer appends to reduce overhead
		if word != "" {
			dict = append(dict, strings.ToLower(word))
		}
		// TODO(ajray): handle errors
		if err != nil { // assume its os.EOF
			break
		}
	}
	// search for word
	sum := scoreList(fields)
	fmt.Println(sum)
}

// test the finding by finding every word in the dictionary
func test() {
	for i, word := range dict {
		if j := findWord(word); i != j {
			if j == -1 {
				fmt.Printf("Failed at %d(%s) got %d\n",i,word,j)
			} else {
				fmt.Printf("Failed at %d(%s) got %d(%s)\n",i,word,j,dict[j])
			}
		}
	}
	fmt.Printf("Passed test \n")
}

