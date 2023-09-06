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

	var p, q int64
	m := int64(1e18)
	Fscan(in, &p, &q)
	n := 1
	for q <= m && q != -1 {
		tmp := q
		q = pow(p, q, m)
		p = tmp
		n++
	}
	Fprintln(out, n)
}

func main() { solve(os.Stdin, os.Stdout) }
func pow(x, n, m int64) int64 {
	res := int64(1)
	if m/n < n {
		return -1
	}
	for ; n > 0; n /= 2 {
		if n%2 > 0 {
			if m/x < res {
				return -1
			}
			res = res * x
		}
		if n > 1 && m/x < x {
			return -1
		}
		x = x * x
		if res > m || x > m {
			return -1
		}
	}
	return res
}
