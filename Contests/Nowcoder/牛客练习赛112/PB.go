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

	var n int
	Fscan(in, &n)
	ans := 0

	pos := make([]int, 31)
	for i := range pos {
		pos[i] = -1
	}

	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
		k := i
		for j := 0; j < 31; j++ {
			if (a[i]>>j)&1 > 0 {
				k = min(k, pos[j])
			} else {
				pos[j] = max(pos[j], i)
			}
		}
		ans += k + 1
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}
