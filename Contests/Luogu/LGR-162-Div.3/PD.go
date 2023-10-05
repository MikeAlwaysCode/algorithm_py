package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	// in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	buf := make([]byte, 4096)
	_i := len(buf)
	rc := func() byte {
		if _i == len(buf) {
			_r.Read(buf)
			_i = 0
		}
		b := buf[_i]
		_i++
		return b
	}
	r := func() (x int) {
		b := rc()
		for ; '0' > b; b = rc() {
		}
		for ; '0' <= b; b = rc() {
			x = x*10 + int(b&15)
		}
		return
	}

	n, m, k, q := r(), r(), r(), r()
	ans := make([]int, k)

	row_vals := make([]int, n)
	col_vals := make([]int, m)
	row_sum, col_sum := 0, 0
	row_nxt := make([]int, n)
	col_nxt := make([]int, m)
	for i := 0; i < n; i++ {
		row_nxt[i] = i + 1
	}
	for i := 0; i < m; i++ {
		col_nxt[i] = i + 1
	}

	modify := func(vals, nxt []int, s *int, l, r int) {
		x := l
		for x <= r {
			if vals[x] == 0 {
				*s++
			}
			vals[x] = 1
			nxt[x], x = nxt[r], nxt[x]
		}
	}

	query := func(vals, nxt []int, l, r int) int {
		res := 0
		for x := l; x <= r; x = nxt[x] {
			res += vals[x] ^ 1
		}
		return res
	}

	qry := make([][]int, q)
	for i := 0; i < q; i++ {
		qry[i] = make([]int, 5)
		qry[i][0], qry[i][1], qry[i][2], qry[i][3], qry[i][4] = r(), r(), r(), r(), r()
		qry[i][3]--
	}

	for i := q - 1; i >= 0; i-- {
		if qry[i][4] == 1 {
			if qry[i][0] == 1 {
				rc, cc := query(row_vals, row_nxt, qry[i][1]-1, qry[i][2]-1), col_sum
				ans[qry[i][3]] += rc * (m - cc)
				modify(row_vals, row_nxt, &row_sum, qry[i][1]-1, qry[i][2]-1)
			} else {
				rc, cc := row_sum, query(col_vals, col_nxt, qry[i][1]-1, qry[i][2]-1)
				ans[qry[i][3]] += (n - rc) * cc
				modify(col_vals, col_nxt, &col_sum, qry[i][1]-1, qry[i][2]-1)
			}
		}
	}

	for i := 0; i < q; i++ {
		if qry[i][4] == 0 {
			if qry[i][0] == 1 {
				rc, cc := query(row_vals, row_nxt, qry[i][1]-1, qry[i][2]-1), col_sum
				ans[qry[i][3]] += rc * (m - cc)
				modify(row_vals, row_nxt, &row_sum, qry[i][1]-1, qry[i][2]-1)
			} else {
				rc, cc := row_sum, query(col_vals, col_nxt, qry[i][1]-1, qry[i][2]-1)
				ans[qry[i][3]] += (n - rc) * cc
				modify(col_vals, col_nxt, &col_sum, qry[i][1]-1, qry[i][2]-1)
			}
		}
	}

	for _, v := range ans {
		Fprint(out, v, " ")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
