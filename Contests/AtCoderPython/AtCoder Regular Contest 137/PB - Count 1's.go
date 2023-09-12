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

	var n, a int
	Fscan(in, &n)
	var mx, mn, pre_mx, pre_mn int
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		pre_mx = max(pre_mx+1-a*2, 1-a*2)
		pre_mn = max(pre_mn+a*2-1, a*2-1)
		mx = max(pre_mx, mx)
		mn = max(pre_mn, mn)
	}

	Fprintln(out, mx+mn+1)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
