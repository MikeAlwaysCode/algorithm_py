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

	var n, ans int
	Fscan(in, &n)
	a := make([]int, n)
	mp := map[int]bool{}
	nz := false
	for i := range a {
		Fscan(in, &a[i])
		mp[a[i]] = true
		if a[i] > 0 {
			nz = true
		}
	}
	if !nz {
		Fprintln(out, 0)
		return
	}
	for mp[ans] {
		ans++
	}
	for i, v := range a {
		if v == 0 {
			if i > 0 {
				ans = max(ans, a[i-1])
			}
			if i < n-1 {
				ans = max(ans, a[i+1])
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
