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

	var T, n, m int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		v, step, s := 1, 1, 1
		for ; m > 0; m-- {
			Fprintln(out, s, s+step, v)
			s++
			if s+step > n {
				s = 1
				step++
			}
			v++
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
