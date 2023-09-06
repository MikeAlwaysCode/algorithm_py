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

	var n, c, a int64
	Fscan(in, &n, &c)
	var ans, mx, k int64 = c * n, 0, 0
	for i := int64(1); i <= n; i++ {
		Fscan(in, &a)
		mx = max(mx, a)
		res := mx + c*(n-i)
		if res < ans {
			ans, k = res, i
		}
	}
	Fprintln(out, k, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int64) int64 {
	if a >= b {
		return a
	} else {
		return b
	}
}
