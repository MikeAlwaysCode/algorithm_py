package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var s string
	Fscan(in, &s)
	cost := [2]int{0, 0}
	for i, c := range s {
		x := int(c - '0')
		cost[0] += ((i & 1) ^ x) * (i + 1)
		cost[1] += ((i & 1) ^ x ^ 1) * (i + 1)
	}
	if cost[0] <= cost[1] {
		Fprintln(out, cost[0])
	} else {
		Fprintln(out, cost[1])
	}
}

func main() { solve(os.Stdin, os.Stdout) }
