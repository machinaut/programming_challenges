// Google Code Jam -- Qualification Round 2011 // Problem B. -- Magicka
// http://code.google.com/codejam/contest/dashboard?c=975485#s=p1
// Alex Ray (2011) <ajray@ncsu.edu>
//
// TODO(ajray):
//  Error checking. For now we assume perfect input
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Combo map[string]string
type Oppos map[string]string

func (c Combo) add(triad string) {
    c[triad[0:2]] = triad[2:]
    c[triad[1:2]+triad[0:1]] = triad[2:]
}
func (o Oppos) add(pair string) {
    o[pair[0:1]]=pair[1:2]
}

// assume we get good input, so ignoring errors here
func main() {
	bufrd := bufio.NewReader(os.Stdin)
	line, _ := bufrd.ReadString('\n')
	T, _ := strconv.Atoi(strings.TrimSpace(line))
	for i := 1; i <= T; i++ {
		line, _ = bufrd.ReadString('\n')
		fields := strings.Fields(line)
		C, _ := strconv.Atoi(fields[0])
        combo := Combo(make(map[string]string,C*2))
        for j := 0 ; j < C ; j++ {
            triad := fields[j+1]
            combo.add(triad)
        }
		D, _ := strconv.Atoi(fields[C+1])
        oppos := Oppos(make(map[string]string,D*2))
        for j := 0 ; j < D ; j++ {
            pair := fields[C+j+2]
            oppos.add(pair)
        }
		N, _ := strconv.Atoi(fields[C+D+2])
        s := fields[C+D+3]
        // TODO(ajray): technically we dont need to rescan whole list,
        // just the changed part. Only really helps for huge cases.
        //fmt.Println(combo,oppos,s)
        out := ""
        for j := 0 ; j < N ; j++ {
            //fmt.Println(j,out)
            out += s[j:j+1]
            for comb, res := range combo {
                out = strings.Replace(out,comb,res,-1)
            }
            for a, b := range oppos {
                if strings.Contains(out,a) && strings.Contains(out,b) {
                    out = ""
                }
            }
        }
		fmt.Printf("Case #%d: [", i)
        for j := 0 ; j < len(out)-1 ; j++ {
            fmt.Printf("%c, ",out[j])
        }
        if len(out) > 1 {
            fmt.Printf("%c]\n",out[len(out)-1])
        } else {
            fmt.Printf("]\n")
        }
	}
}
