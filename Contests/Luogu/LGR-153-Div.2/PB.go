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

	var n int
	Fscan(in, &n)
	if n&1 > 0 {
		Fprint(out, n, " ")
		for i := 1; i < n; i += 2 {
			Fprint(out, i, " ", n-i, " ")
		}
		Fprintln(out)
	} else {
		Fprint(out, n, " ")
		for i := 1; i <= n-i; i += 2 {
			Fprint(out, i, " ")
			if n-i > i {
				Fprint(out, n-i, " ")
			}
		}
		v := make([]int, n/2-1)
		for i := 2; i <= n-i; i += 2 {
			v[i-2] = i
			if n-i > i {
				v[i-1] = n - i
			}
		}
		for i := n/2 - 2; i >= 0; i-- {
			Fprint(out, v[i], " ")
		}
		Fprintln(out)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
