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

	var n, m, b int
	var l, r int
	Fscan(in, &n, &m)
	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
		if a[i] > r {
			r = a[i]
		}
	}
	pay := make([]bool, n)
	for i := 0; i < m; i++ {
		Fscan(in, &b)
		b--
		pay[b] = true
	}
	check := func(x int) bool {
		h := make([]int, n)
		d := make([]int, n)

		s, c := 0, 0
		for i := 0; i < n; i++ {
			c += d[i]
			d[i] = 0
			s -= c
			h[i] += s
			if pay[i] {
				s += x
				c++
				if i+x+1 < n {
					d[i+x+1] -= 1
				}
			}
		}
		s, c = 0, 0
		for i := n - 1; i >= 0; i-- {
			c += d[i]
			s -= c
			h[i] += s
			if pay[i] {
				s += x
				c++
				if i-x-1 >= 0 {
					d[i-x-1] -= 1
				}
			}
		}

		for i, v := range h {
			if pay[i] {
				v += x
			}
			if v < a[i] {
				return false
			}
		}
		return true
	}

	r += n
	for l < r {
		m = (l + r) >> 1
		if check(m) {
			r = m
		} else {
			l = m + 1
		}
	}
	Fprintln(out, r)
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
