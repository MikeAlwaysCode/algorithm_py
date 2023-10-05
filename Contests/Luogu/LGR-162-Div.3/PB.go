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

	var a, b, c, m, op, k int
	Fscan(in, &a, &b, &c, &m)
	la, lb, lc := a, b, c
	for i := 0; i < m; i++ {
		Fscan(in, &op, &k)
		if op == 1 {
			la = min(la, a-k)
		} else if op == 2 {
			lb = min(lb, b-k)
		} else {
			lc = min(lc, c-k)
		}
		Fprintln(out, la*lb*lc)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
