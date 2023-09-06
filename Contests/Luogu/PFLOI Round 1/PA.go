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

	var n, p int
	var m, x, mx int64
	Fscan(in, &n, &m, &x, &p)
	a := make([]int64, n)
	for i := range a {
		Fscan(in, &a[i])
		mx = max(mx, a[i])
	}

	if mx <= m {
		Fprintln(out, 0)
	} else {
		Fprintln(out, (mx-m+x-1)/x)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int64) int64 {
	if a >= b {
		return a
	} else {
		return b
	}
}
