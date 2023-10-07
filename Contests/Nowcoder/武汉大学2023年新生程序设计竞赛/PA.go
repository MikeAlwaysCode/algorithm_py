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

	var n int
	Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
	}
	sort.Ints(a)
	if a[0] > 1 {
		Fprintln(out, "NO")
		return
	}
	for i := 1; i < n; i++ {
		if a[i] > a[i-1]+1 {
			Fprintln(out, "NO")
			return
		}
	}
	Fprintln(out, "YES")
}

func main() { solve(os.Stdin, os.Stdout) }
