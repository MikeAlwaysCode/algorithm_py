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

	var n, m, p int
	Fscan(in, &n, &m, &p)
	a := make([]int, n)
	b := make([]int, m)
	for i := range a {
		Fscan(in, &a[i])
	}
	for i := range b {
		Fscan(in, &b[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(a)))
	sort.Ints(b)
	var ans, s, j int
	for _, v := range a {
		for j < m && v+b[j] <= p {
			s += b[j]
			j++
		}
		ans += v*j + s + p*(m-j)
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
