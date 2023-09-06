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

	var n, h, k, a, b int
	Fscan(in, &n, &h, &k)
	blood := make([]int, n)
	for i := range blood {
		Fscan(in, &a, b)
		t := a/4*3 - 1
		if a%4 > 0 {
			if a%4 < 3 {
				t += 1
			} else {
				t += 2
			}
		}
		blood[i] = t * b
	}
	sort.Ints(blood)
	for i := 1; i < n; i++ {
		blood[i] += blood[i-1]
	}
	var q, x int
	for Fscan(in, &q); q > 0; q-- {
		Fscan(in, &x)
		ans := sort.SearchInts(blood, h+x*k)
		Fprint(out, ans, " ")
	}
	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
