package main

import (
	"bufio"
	. "fmt"
	"io"
	"math/big"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, m int
	var s string
	Fscan(in, &n, &m)
	up := make([][]int, n)
	left := make([][]int, n)
	ans := big.NewInt(0)
	for i := range up {
		up[i] = make([]int, m)
		left[i] = make([]int, m)
		Fscan(in, &s)
		for j, c := range s {
			if c == '#' {
				up[i][j] = 1
				left[i][j] = 1
				if i > 0 {
					up[i][j] += up[i-1][j]
				}
				if j > 0 {
					left[i][j] += left[i][j-1]
				}
				ans.Add(ans, big.NewInt(int64(up[i][j]*up[i][j])))
				ans.Add(ans, big.NewInt(int64(left[i][j]*left[i][j])))
			}
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
