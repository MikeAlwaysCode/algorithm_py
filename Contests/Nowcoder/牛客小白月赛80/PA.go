package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

type matrix [][]int

const mod int = 998244353

func newMatrix(n, m int) matrix {
	a := make(matrix, n)
	for i := range a {
		a[i] = make([]int, m)
	}
	return a
}

func newIdentityMatrix(n int) matrix {
	a := make(matrix, n)
	for i := range a {
		a[i] = make([]int, n)
		a[i][i] = 1
	}
	return a
}

func (a matrix) mul(b matrix) matrix {
	c := newMatrix(len(a), len(b[0]))
	for i, row := range a {
		for j := range b[0] {
			for k, v := range row {
				c[i][j] = (c[i][j] + v*b[k][j]) % mod
			}
			if c[i][j] < 0 {
				c[i][j] += mod
			}
		}
	}
	return c
}

func (a matrix) pow(n int) matrix {
	res := newIdentityMatrix(len(a))
	for ; n > 0; n /= 2 {
		if n%2 > 0 {
			res = res.mul(a)
		}
		a = a.mul(a)
	}
	return res
}

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	Fscan(in, &n)
	if n == 1 {
		Fprintln(out, 2)
		return
	}
	m := matrix{
		{2, -1},
		{1, 0},
	}.pow(n - 1)
	Fprintln(out, (m[0][0]*2+m[0][1])%mod)
}

func main() { solve(os.Stdin, os.Stdout) }
