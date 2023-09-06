package main

import (
	"bufio"
	// "container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, m, x int
	Fscan(in, &n, &m)
	a := make([]int, n)
	b := make([]int, m)
	for i := range a {
		Fscan(in, &a[i])
	}
	for i := range b {
		Fscan(in, &b[i])
	}
	Fscan(in, &x)
	ans := 0
	for i := 0; i < n; i++ {
		sa := 0
		for j := i; j < n; j++ {
			sa += a[j]
			if sa > x {
				break
			}
			for k := 0; k < m; k++ {
				ss := 0
				for l := k; l < m; l++ {
					ss += b[l] * sa
					if ss > x {
						break
					}
					ans = max(ans, (j-i+1)*(l-k+1))
				}
			}
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
