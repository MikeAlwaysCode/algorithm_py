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
		var ans, s int
		idx := make([]int, n)
		a := make([]int, n)
		for i := range a {
			Fscan(in, &a[i])
			idx[i] = i
		}
		b := make([]int, n)
		for i := range b {
			Fscan(in, &b[i])
			ans += b[i]
			s += b[i]
		}

		sort.Slice(idx, func(i, j int) bool {
			return a[idx[i]] <= a[idx[j]]
		})

		for _, i := range idx {
			s -= b[i]
			ans = min(ans, max(a[i], s))
		}

		Fprintln(out, ans)
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
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
