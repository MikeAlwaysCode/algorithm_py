package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		s := []int{}
		for p := 1; n > 0; p *= 2 {
			m := min(p, n)
			s = append(s, m)
			n -= m
		}
		sort.Ints(s)
		Fprintln(out, len(s)-1)
		for i := 1; i < len(s); i++ {
			Fprint(out, s[i]-s[i-1], " ")
		}
		Fprintln(out)
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
