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

	var n, p int
	Fscan(in, &n)
	ans := 0
	for i := 0; i < n; i++ {
		Fscan(in, &p)
		ans += 21 - p
		if p&1 > 0 {
			ans -= p + 1
		} else {
			ans -= p - 1
		}
		if i == n-1 {
			ans += p
		}
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
