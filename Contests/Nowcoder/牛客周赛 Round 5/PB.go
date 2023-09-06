package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, k int
	Fscan(in, &n, &k)
	ans := make([]int, n)
	l, r := 1, n-k+1
	for i := range ans {
		if r <= n && i%2 == 0 {
			ans[i] = r
			r++
		} else {
			ans[i] = l
			l++
		}
	}

	for _, v := range ans {
		Fprint(out, v, " ")
	}
	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
