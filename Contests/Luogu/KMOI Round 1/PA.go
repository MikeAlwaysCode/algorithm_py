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

	var l, r, k int
	Fscan(in, &l, &r, &k)
	if k == 1 {
		Fprintln(out, 0)
		return
	}
	ans := 0
	if l == 1 {
		ans = 1
	}
	s := 1
	for i := 2; i <= min(r, k-1); i++ {
		s = s * i % k
		if s == 0 {
			break
		}
		if i >= l {
			ans = max(ans, s)
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
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
