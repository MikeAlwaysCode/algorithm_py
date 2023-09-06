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

	var n, m, p, s int
	Fscan(in, &n, &m)
	mp := map[int]int{}
	for i := 0; i < n; i++ {
		Fscan(in, &p)
		mp[p] = 0
	}
	for i := 0; i < m; i++ {
		Fscan(in, &p, &s)
		if s >= 60 {
			mp[p] = 2
		} else {
			mp[p] = 1
		}
	}
	ans := [3]int{0, 0, 0}
	for _, v := range mp {
		ans[v]++
	}
	Fprintln(out, ans[0])
	Fprintln(out, ans[0]+ans[1])
}

func main() { solve(os.Stdin, os.Stdout) }
