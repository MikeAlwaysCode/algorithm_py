package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strconv"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	var x int64
	Fscan(in, &n, &x)
	m := map[int64]int{}
	m[x] = 0
	q := []int64{x}
	for len(q) > 0 {
		x = q[0]
		q = q[1:]
		s := strconv.FormatInt(x, 10)
		if len(s) == n {
			Fprintln(out, m[x])
			return
		}
		for _, c := range s {
			nxt := x * int64(c-'0')
			if _, ok := m[nxt]; !ok {
				m[nxt] = m[x] + 1
				q = append(q, nxt)
			}
		}
	}
	Fprintln(out, -1)
}

func main() { solve(os.Stdin, os.Stdout) }
