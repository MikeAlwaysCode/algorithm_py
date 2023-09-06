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

	var n, m, l int
	Fscan(in, &n, &m, &l)
	mp := map[string]bool{}
	var s string
	for i := 0; i < n; i++ {
		Fscan(in, &s)
		mp[s] = true
	}
	for i := 0; i < m; i++ {
		Fscan(in, &s)
		mp[s] = false
	}
	for i := 0; i < l; i++ {
		Fscan(in, &s)
		mp[s] = true
	}

	ans := []string{}
	for k, v := range mp {
		if v {
			ans = append(ans, k)
		}
	}
	sort.Strings(ans)
	for _, v := range ans {
		Fprintln(out, v)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
