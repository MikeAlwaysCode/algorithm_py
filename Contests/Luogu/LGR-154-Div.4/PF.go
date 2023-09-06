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

	var r, c, n, m int
	Fscan(in, &r, &c, &n, &m)
	g := make([]string, r)
	cnt := make([][]int, r)
	for i := range g {
		cnt[i] = make([]int, c)
		Fscan(in, &g[i])
	}
	col_m := make([]int, c)
	col_f := make([]int, c)
	row_m := make([]int, r)
	row_f := make([]int, r)
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			if g[i][j] == 'F' {
				cnt[i][j] += min(1, col_m[j]) + min(1, row_m[i])
				col_f[j]++
				row_f[i]++
			} else if g[i][j] == 'M' {
				cnt[i][j] += min(1, col_f[j]) + min(1, row_f[i])
				col_m[j]++
				row_m[i]++
			}
		}
	}
	for i := 0; i < c; i++ {
		col_m[i] = 0
		col_f[i] = 0
	}
	for i := 0; i < r; i++ {
		row_m[i] = 0
		row_f[i] = 0
	}

	for i := r - 1; i >= 0; i-- {
		for j := c - 1; j >= 0; j-- {
			if g[i][j] == 'F' {
				cnt[i][j] += min(1, col_m[j]) + min(1, row_m[i])
				col_f[j]++
				row_f[i]++
			} else if g[i][j] == 'M' {
				cnt[i][j] += min(1, col_f[j]) + min(1, row_f[i])
				col_m[j]++
				row_m[i]++
			}
		}
	}

	ans := 0
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			if g[i][j] != '.' && cnt[i][j] <= 1 {
				ans++
			}
		}
	}
	Fprintln(out, ans)

}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
