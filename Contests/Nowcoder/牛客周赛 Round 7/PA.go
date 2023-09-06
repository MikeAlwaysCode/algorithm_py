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

	var n, m int
	Fscan(in, &n, &m)
	s := make([]string, n)
	for i := range s {
		Fscan(in, &s[i])
	}

	check := func(i, j int) bool {
		mp := map[byte]bool{}
		mp[s[i][j]] = true
		mp[s[i][j+1]] = true
		mp[s[i+1][j]] = true
		mp[s[i+1][j+1]] = true
		t := "you"
		for _, c := range t {
			if _, ok := mp[byte(c)]; !ok {
				return false
			}
		}
		return true
	}

	ans := 0
	for i := 0; i < n-1; i++ {
		for j := 0; j < m-1; j++ {
			if check(i, j) {
				ans++
			}
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
