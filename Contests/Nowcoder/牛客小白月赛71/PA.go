package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var a, b, c, d int
	Fscan(in, &a, &b, &c, &d)
	if (c >= a && d >= b) || (c >= b && d >= a) {
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
