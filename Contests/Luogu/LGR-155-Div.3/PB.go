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

	var n, m int
	var s string
	Fscan(in, &n, &m, &s)
	idx := 0
	ans := make([]int, m)
	for i, c := range s {
		if c == 'N' {
			idx++
			if idx > n {
				Fprintln(out, "No solution")
				return
			}
			ans[i] = idx
		} else {
			if idx < 1 {
				Fprintln(out, "No solution")
				return
			}
			ans[i] = 1
		}
	}
	for _, v := range ans {
		Fprint(out, v, " ")
	}
	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
