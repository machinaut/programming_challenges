// Google Code Jam -- Qualification Round 2011
// Problem A. -- Bot Trust
// http://code.google.com/codejam/contest/dashboard?c=975485
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

// return the other bot's string
func o(bot string) string {
    if bot == "O" {
        return "B"
    }
    return "O"
}

// absolute value
func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}

// assume we get good input, so ignoring errors here
func main() {
	bufrd := bufio.NewReader(os.Stdin)
    line,_ := bufrd.ReadString('\n')
    nCase, _ := strconv.Atoi(strings.TrimSpace(line))
    bots := make(map[string]int,2)
    wait := make(map[string]int,2)
    for i := 1 ; i <= nCase ; i++ {
        time := 0
        bots["O"] = 1 // orange
        bots["B"] = 1 // blue
        wait["O"] = 0
        wait["B"] = 0
        caseline,_ := bufrd.ReadString('\n')
        fields := strings.Fields(caseline)
        nStep, _ := strconv.Atoi(fields[0])
        for j := 0 ; j < nStep ; j++ {
            // which bot has to move, and where to
            bot := fields[2*j+1]
            button,_ := strconv.Atoi(fields[2*j+2])
            // distance to travel, less the time we could have been traveling
            dist := abs(button - bots[bot]) - wait[bot]
            bots[bot] = button
            // update the wait values and time
            wait[bot] = 0
            wait[o(bot)] += 1
            time += 1
            if dist > 0 {
                wait[o(bot)] += dist
                time += dist
            }
        }
        fmt.Printf("Case #%d: %d\n",i,time)
    }
}

