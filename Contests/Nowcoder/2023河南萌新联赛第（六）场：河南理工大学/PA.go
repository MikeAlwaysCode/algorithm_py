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

	var n, a int
	Fscan(in, &n)
	cnt := make([][]int, 31)
	for i := range cnt {
		cnt[i] = make([]int, n+1)
	}

	for i := 1; i <= n; i++ {
		Fscan(in, &a)
		for j := 0; j < 31; j++ {
			cnt[j][i] = cnt[j][i-1] + (a>>j)&1
		}
	}

	var q, l, r int
	for Fscan(in, &q); q > 0; q-- {
		Fscan(in, &l, &r)
		ans := 0
		for j := 0; j < 31; j++ {
			if (cnt[j][r]-cnt[j][l-1])*2 < r-l+1 {
				ans |= 1 << j
			}
		}
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
