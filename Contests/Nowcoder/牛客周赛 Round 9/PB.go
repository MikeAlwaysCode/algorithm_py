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

	var n int
	Fscan(in, &n)
	var s, ans int64
	a := make([]int64, n)
	for i := range a {
		Fscan(in, &a[i])
		s += a[i]
	}
	ans = s
	for i := 1; i < n; i++ {
		ans = max(ans, s-a[i]-a[i-1]+a[i]*a[i-1])
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int64) int64 {
	if a >= b {
		return a
	} else {
		return b
	}
}
